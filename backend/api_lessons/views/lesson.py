from pprint import pprint

from rest_framework.request import Request
from rest_framework.views import APIView
from api_lessons.models import *
from api_lessons.serializers import *
from api_lessons.serializers import *
from api_users.serializers import UserModelSerializer
from backend.global_function import *


class GetLessonsBatchView(APIView):
    def get(self, request):
        lessons_batch = LessonBatch.objects.all()
        return success_with_text(LessonBatchSerializer(lessons_batch, user=request.user, many=True).data)


class GetLessonView(APIView):
    def post(self, request):
        serializer = GetLessonById(data=request.data)
        serializer.is_valid(raise_exception=True)
        lesson: Lesson = serializer.validated_data['lesson_id']
        user: UserModel = request.user
        if not lesson.is_available_for_user(user):
            return error_with_text('lesson_not_available')

        lesson_before = Lesson.objects.filter(lesson_batch=lesson.lesson_batch, order=lesson.order - 1).first()
        if lesson_before:
            if not UserLessonModel.objects.filter(user=user, lesson=lesson_before, completed=True).exists():
                return error_with_text('unlock_prev_lesson')

        UserLessonModel.objects.get_or_create(user=user, lesson=lesson)
        return success_with_text(LessonSerializer(lesson, context={'user': user}).data)


class CheckLessonForEnding(APIView):
    def post(self, request: Request):
        serializer = GetLessonById(data=request.data)
        serializer.is_valid(raise_exception=True)
        lesson: Lesson = serializer.validated_data['lesson_id']
        ans = lesson.is_lesson_done_for_user(request.user)
        if ans == 'ok':
            user_lesson = UserLessonModel.objects.get_or_create(user=request.user, lesson=lesson)[0]
            user_lesson.completed = True
            user_lesson.save()
            return success_with_text(UserModelSerializer(request.user).data)
        return error_with_text(ans)


class AddLessonToBatchView(APIView):
    def post(self, request: Request):
        # delete all lessons
        Lesson.objects.all().delete()

        lesson_serializer = LessonSerializer(data=request.data, user=request.user)
        lesson_serializer.is_valid(raise_exception=True)
        lesson: Lesson = lesson_serializer.save()
        return success_with_text(LessonSerializer(lesson, user=request.user).data)
