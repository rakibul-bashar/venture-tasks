from django_filters import FilterSet, DateFromToRangeFilter, CharFilter
from django_filters.widgets import RangeWidget

from .models import (
    Project,
    Log,
)
class LogListFilters(FilterSet):
    date = DateFromToRangeFilter(
        widget=RangeWidget(attrs={'placeholder': 'YYYY-MM-DD'}),
        name="task_date")
    project_name = CharFilter(name="project__name")
    working_hour = CharFilter(name="working_hour")

    # pylint: disable=old-style-class, no-init
    class Meta:
        model = Log
        fields = [
            'working_hour',
        ]
