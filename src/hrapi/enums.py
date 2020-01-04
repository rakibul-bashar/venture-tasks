from django.utils.translation import gettext as _
from enumerify.enum import Enum

class LocationType(Enum):
    INSIDE = 1
    OUTSIDE = 2

    i18n = (
        _('Inside'),
        _('Outside'),
    )