from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from common.api.mixin import InterestWiseOrderMixin, PublishableModelMixin
from common.paginations import StandardResultsSetPagination
from courses.api.permissions import IsCourseEnrolledActive
from courses.api.serializers import (
    CourseCategoryRetrieveSerializer,
    CourseListSerializer,
    CourseRetrieveSerializerAfterEnroll,
    CourseRetrieveSerializerBeforeEnroll,
)
from courses.filters import CourseFilter
from courses.models import Course, CourseCategory


class CourseListAPIView(PublishableModelMixin, InterestWiseOrderMixin, ListAPIView):
    """View for listing courses."""

    permission_classes = [AllowAny]
    serializer_class = CourseListSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ["name"]
    queryset = Course.objects.all()
    filterset_class = CourseFilter
    pagination_class = StandardResultsSetPagination
    # filterset_fields = ['price', 'category']
    # ordering = ['course']

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class CourseRetrieveAPIAfterEnrollView(PublishableModelMixin, RetrieveAPIView):
    """View for retrieving courses."""

    permission_classes = [IsAuthenticated, IsCourseEnrolledActive]
    serializer_class = CourseRetrieveSerializerAfterEnroll
    queryset = Course.objects.all()


class CourseRetrieveAPIBeforeEnrollView(PublishableModelMixin, RetrieveAPIView):
    """View for retrieving courses."""

    permission_classes = [IsAuthenticated]
    serializer_class = CourseRetrieveSerializerBeforeEnroll
    queryset = Course.objects.all()


class CourseCategoryListAPIView(ListAPIView):
    """View for listing course categories."""

    permission_classes = [AllowAny]
    serializer_class = CourseCategoryRetrieveSerializer
    queryset = CourseCategory.objects.all()


class CourseCategoryRetrieveAPIView(RetrieveAPIView):
    """View for retrieving course categories."""

    permission_classes = [AllowAny]
    serializer_class = CourseCategoryRetrieveSerializer
    queryset = CourseCategory.objects.all()
