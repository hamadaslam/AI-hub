from django.contrib import admin
from .models import *
# Register your models here.
# from .models import PROJECT_PARTNER
# from .models import RESEARCH_CENTRE
# from .models import FISCAL_YEAR
# from .models import DEPARTMENT
# from .models import Program
# from .models import FACULTY
# from .models import Project
# from .models import FUNDER
# from .models import NAICS_CLASSIFICATION
# from .models import REVIEW
# from .models import FINANCE
# from .models import STUDENT

admin.site.register(PROJECT_PARTNER)
admin.site.register(RESEARCH_CENTRE)
admin.site.register(FISCAL_YEAR)
admin.site.register(DEPARTMENT)
admin.site.register(Program)
admin.site.register(FACULTY)
admin.site.register(Project)
admin.site.register(FUNDER)
admin.site.register(NAICS_CLASSIFICATION)
admin.site.register(REVIEW)
admin.site.register(FINANCE)
admin.site.register(STUDENT)
admin.site.register(FUNDING_LEVEL)
admin.site.register(INDUSTRY_SIZE)
admin.site.register(RESOURCE)