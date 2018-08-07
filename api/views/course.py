from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.versioning import URLPathVersioning
from api.serializers.course import CourseSerializer
from api import models
from rest_framework.response import Response


class CoursesView(APIView):

    def get(self, request, *args, **kwargs):
        # a.查看所有学位课并打印学位课名称以及授课老师
        course_list = models.DegreeCourse.objects.values('name', 'teachers')
        # b.查看所有学位课并打印学位课名称以及学位课的奖学金

        # c.展示所有的专题课

        # d. 查看id=1的学位课对应的所有模块名称

        # e.获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses

        # f.获取id = 1的专题课，并打印该课程相关的所有常见问题

        # g.获取id = 1的专题课，并打印该课程相关的课程大纲

        # h.获取id = 1的专题课，并打印该课程相关的所有章节
        #

        ser = CourseSerializer(instance=course_list, many=True)

        return Response(ser.data)
