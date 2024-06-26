from rest_framework import serializers
from api_lessons.models import *
from backend.global_function import UserContextNeededSerializer


class LessonMinimalDataSerializer(UserContextNeededSerializer, serializers.ModelSerializer):
    completed = serializers.SerializerMethodField()
    friends_count = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = ['id', 'is_available_on_free', 'completed', 'friends_count']

    def get_completed(self, obj):
        user_data = UserLessonModel.objects.filter(user=self.user, lesson=obj).first()
        if user_data:
            return user_data.completed
        return False

    def get_friends_count(self, obj: Lesson):
        counter = 0
        for i in self.user.friends.all():
            last_lesson = i.lessons.last()
            if last_lesson:
                if last_lesson.lesson == obj:
                    counter += 1
        return counter


class LessonBatchSerializer(UserContextNeededSerializer, serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField()

    class Meta:
        model = LessonBatch
        fields = '__all__'

    def get_lessons(self, obj):
        return LessonMinimalDataSerializer(obj.lessons.all(), user=self.user, many=True).data


class QuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswer
        fields = '__all__'


class VideoComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoComponent
        fields = '__all__'


class ConspectusComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConspectusComponent
        fields = '__all__'


class QuestionComponentSerializer(UserContextNeededSerializer, serializers.ModelSerializer):
    answers = QuestionAnswerSerializer(many=True)
    is_user_answered = serializers.SerializerMethodField()

    class Meta:
        model = QuestionComponent
        fields = '__all__'

    def get_is_user_answered(self, obj):
        return UserQuestionModel.objects.filter(user=self.user, question=obj).exists()


class LessonComponentSerializer(UserContextNeededSerializer, serializers.ModelSerializer):
    conspectus_component = ConspectusComponentSerializer()
    video_component = VideoComponentSerializer()
    question_component = serializers.SerializerMethodField()

    class Meta:
        model = LessonComponent
        fields = '__all__'

    def get_question_component(self, obj):
        if obj.question_component:
            return QuestionComponentSerializer(obj.question_component, user=self.user).data
        return None


class LessonSerializer(UserContextNeededSerializer, serializers.ModelSerializer):
    lesson_components = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = '__all__'

    def get_lesson_components(self, instance):
        return LessonComponentSerializer(instance.components.all(), user=self.user, many=True).data
