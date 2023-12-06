from .models import *
from django.contrib import admin
admin.site.site_url = '/passingDashboard'
admin.site.register(AccountAddresses)

@admin.register(Accounts)
class AccountsAdmin(admin.ModelAdmin):
    list_display = ('accountid','pageid','accountemail','accountphonenum','accountdate','subscriptiontype')
    ordering = ('accountid',)
    search_fields = ('accountid','')
admin.site.register(Advertisements)
admin.site.register(Applications)
admin.site.register(Article)
admin.site.register(Bank)
admin.site.register(CertMaterials)
admin.site.register(Certifications)
admin.site.register(Choose)
admin.site.register(Companies)
admin.site.register(Comprises)
admin.site.register(Connections)
admin.site.register(Contain)
admin.site.register(CertifiedCourses)
admin.site.register(CreditCard)
admin.site.register(Employees)
admin.site.register(Employers)
admin.site.register(EmploymentRecord)
admin.site.register(Event)
admin.site.register(FillOut)
admin.site.register(Free)
# admin.site.register(GroupTags)
admin.site.register(Groups)
admin.site.register(Images)
admin.site.register(IndividualUsers)
admin.site.register(Interview)
admin.site.register(InvoiceOrders)
admin.site.register(JobSeekers)
admin.site.register(Jobs)
admin.site.register(Lessons)
admin.site.register(Link)
admin.site.register(Messages)
admin.site.register(Organizations)
admin.site.register(Pages)
admin.site.register(PaymentTypes)
admin.site.register(PostComments)
admin.site.register(PostLikes)
admin.site.register(Posts)
admin.site.register(Premium)
admin.site.register(Quizzes)
admin.site.register(Reactions)
admin.site.register(ReactsTo)
admin.site.register(Results)
admin.site.register(Scores)
admin.site.register(SettingDetails)
admin.site.register(Settings)
# admin.site.register(Subscriptiontype)
admin.site.register(Tags)
admin.site.register(Teach)
admin.site.register(TeacherExpertise)
admin.site.register(Teachers)
admin.site.register(Text)
admin.site.register(Uploads)
admin.site.register(ViewsCount)

