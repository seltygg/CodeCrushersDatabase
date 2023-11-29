# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

class AccountAddresses(models.Model):
    accountid = models.OneToOneField('Accounts', models.DO_NOTHING, db_column='accountid', primary_key=True)
    addressstreet = models.CharField(max_length=255, blank=True, null=True)
    addresscity = models.CharField(max_length=255, blank=True, null=True)
    addressstate = models.CharField(max_length=255, blank=True, null=True)
    addresscountry = models.CharField(max_length=255, blank=True, null=True)
    addresszipcode = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_addresses'
        verbose_name_plural = 'Account Address'


class Accounts(models.Model):
    accountid = models.CharField(primary_key=True, max_length=10)
    pageid = models.ForeignKey('Pages', models.DO_NOTHING, db_column='pageid', blank=True, null=True)
    accountemail = models.EmailField(unique=True, max_length=255, blank=True, null=True)
    accountpassword = models.CharField(max_length=255, blank=True, null=True)
    accountphonenum = models.CharField(unique=True, max_length=11, blank=True, null=True)
    accountdate = models.DateField(blank=True, null=True)
    submodelid = models.ForeignKey('Subscriptiontype', models.DO_NOTHING, db_column='submodelid', blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    accountlogofilepath = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts'
        verbose_name_plural = 'Accounts'
        


class Advertisements(models.Model):
    advertisementid = models.CharField(primary_key=True, max_length=10)
    advertisementtype = models.CharField(max_length=50, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    submodelid = models.ForeignKey('Free', models.DO_NOTHING, db_column='submodelid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'advertisements'
        verbose_name_plural = 'Advertisements'


class Applications(models.Model):
    applicationid = models.OneToOneField('JobSeekers', models.DO_NOTHING, db_column='applicationid', primary_key=True)
    jobid = models.ForeignKey('Jobs', models.DO_NOTHING, db_column='jobid', blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    dateapplied = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'applications'
        verbose_name_plural = 'Applications'


class Applies(models.Model):
    jobid = models.CharField(max_length=10, blank=True, null=True)
    jobseekerid = models.ForeignKey('JobSeekers', models.DO_NOTHING, db_column='jobseekerid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'applies'
        verbose_name_plural = 'Applies'


class Article(models.Model):
    postid = models.OneToOneField('Posts', models.DO_NOTHING, db_column='postid', primary_key=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    articletitle = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article'
        verbose_name_plural = 'Article'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bank(models.Model):
    paymentid = models.OneToOneField('Paymenttypes', models.DO_NOTHING, db_column='paymentid', primary_key=True)
    accountid = models.CharField(max_length=10, blank=True, null=True)
    paymentname = models.CharField(max_length=50, blank=True, null=True)
    paymenttype = models.CharField(max_length=50, blank=True, null=True)
    backacctnum = models.FloatField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bank'
        verbose_name_plural = 'Bank'


class CertMaterials(models.Model):
    fileid = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'cert_materials'
        verbose_name_plural = 'CertMaterials'


class Certificates(models.Model):
    certificateid = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    topic = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'certificates'
        verbose_name_plural = 'Certificates'


class Choose(models.Model):
    tagid = models.OneToOneField('Tags', models.DO_NOTHING, db_column='tagid', primary_key=True)  # The composite primary key (tagid, useraccountid) found, that is not supported. The first column is selected.
    useraccountid = models.ForeignKey('IndividualUsers', models.DO_NOTHING, db_column='useraccountid')

    class Meta:
        managed = False
        db_table = 'choose'
        unique_together = (('tagid', 'useraccountid'),)
        verbose_name_plural = 'Choose'


class Companies(models.Model):
    companyaccountid = models.OneToOneField(Accounts, models.DO_NOTHING, db_column='companyaccountid', primary_key=True)
    companyname = models.CharField(max_length=255, blank=True, null=True)
    numberemp = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'companies'
        verbose_name_plural = 'Companies'


class Comprises(models.Model):
    accountid = models.OneToOneField('IndividualUsers', models.DO_NOTHING, db_column='accountid', primary_key=True)  # The composite primary key (accountid, groupid) found, that is not supported. The first column is selected.
    groupid = models.ForeignKey('Groups', models.DO_NOTHING, db_column='groupid')

    class Meta:
        managed = False
        db_table = 'comprises'
        unique_together = (('accountid', 'groupid'),)
        verbose_name_plural = 'Comprises'


class Connections(models.Model):
    senderid = models.OneToOneField('IndividualUsers', models.DO_NOTHING, db_column='senderid', primary_key=True)  # The composite primary key (senderid, receiverid, ctimestamp) found, that is not supported. The first column is selected.
    receiverid = models.ForeignKey('IndividualUsers', models.DO_NOTHING, db_column='receiverid', related_name='connections_receiverid_set')
    ctimestamp = models.DateTimeField()
    greeting = models.CharField(max_length=255, blank=True, null=True)
    cstatus = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'connections'
        unique_together = (('senderid', 'receiverid', 'ctimestamp'),)
        verbose_name_plural = 'Connections'


class Contain(models.Model):
    fileid = models.OneToOneField(CertMaterials, models.DO_NOTHING, db_column='fileid', primary_key=True)  # The composite primary key (fileid, certificateid) found, that is not supported. The first column is selected.
    certificateid = models.ForeignKey(Certificates, models.DO_NOTHING, db_column='certificateid')

    class Meta:
        managed = False
        db_table = 'contain'
        unique_together = (('fileid', 'certificateid'),)
        verbose_name_plural = 'Contain'


class Courses(models.Model):
    courseid = models.CharField(primary_key=True, max_length=10)
    coursename = models.CharField(max_length=255, blank=True, null=True)
    duration = models.BigIntegerField(blank=True, null=True)
    certificateid = models.ForeignKey(Certificates, models.DO_NOTHING, db_column='certificateid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'courses'
        verbose_name_plural = 'Courses'


class Creditcard(models.Model):
    paymentid = models.OneToOneField('Paymenttypes', models.DO_NOTHING, db_column='paymentid', primary_key=True)
    accountid = models.CharField(max_length=10, blank=True, null=True)
    paymentname = models.CharField(max_length=50, blank=True, null=True)
    paymenttype = models.CharField(max_length=50, blank=True, null=True)
    ccnum = models.FloatField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'creditcard'
        verbose_name_plural = 'Creditcard'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employees(models.Model):
    employeeid = models.OneToOneField('IndividualUsers', models.DO_NOTHING, db_column='employeeid', primary_key=True)
    jobtitle = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'
        verbose_name_plural = 'Employees'


class Employers(models.Model):
    employerid = models.OneToOneField('IndividualUsers', models.DO_NOTHING, db_column='employerid', primary_key=True)
    companyname = models.CharField(max_length=255, blank=True, null=True)
    sponsorship = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employers'
        verbose_name_plural = 'Employers'


class EmploymentRecord(models.Model):
    employmentrecordid = models.CharField(primary_key=True, max_length=10)
    employeeid = models.ForeignKey(Employees, models.DO_NOTHING, db_column='employeeid', blank=True, null=True)
    organizationid = models.ForeignKey('Organizations', models.DO_NOTHING, db_column='organizationid', blank=True, null=True)
    workbegindate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employment_record'
        verbose_name_plural = 'EmploymentRecord'


class Event(models.Model):
    postid = models.OneToOneField('Posts', models.DO_NOTHING, db_column='postid', primary_key=True)
    name = models.CharField(max_length=255)
    eventdescription = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    currdate = models.DateField(blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True, null=True)
    eventlocation = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event'
        verbose_name_plural = 'Event'


class FillOut(models.Model):
    applicationid = models.OneToOneField(Applications, models.DO_NOTHING, db_column='applicationid', primary_key=True)  # The composite primary key (applicationid, jobseekerid) found, that is not supported. The first column is selected.
    jobseekerid = models.ForeignKey('JobSeekers', models.DO_NOTHING, db_column='jobseekerid')
    jobtitle = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fill_out'
        unique_together = (('applicationid', 'jobseekerid'),)
        verbose_name_plural = 'FillOut'


class Followings(models.Model):
    followerpageid = models.ForeignKey('Pages', models.DO_NOTHING, db_column='followerpageid')
    followeepageid = models.OneToOneField('Pages', models.DO_NOTHING, db_column='followeepageid', primary_key=True, related_name='followings_followeepageid_set')  # The composite primary key (followeepageid, followerpageid, timestamp) found, that is not supported. The first column is selected.
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'followings'
        unique_together = (('followeepageid', 'followerpageid', 'timestamp'),)
        verbose_name_plural = 'Followings'


class Free(models.Model):
    submodelid = models.OneToOneField('Subscriptiontype', models.DO_NOTHING, db_column='submodelid', primary_key=True)
    subscriptiontype = models.CharField(max_length=50, blank=True, null=True)
    adpreferences = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'free'
        verbose_name_plural = 'Free'


class GroupTags(models.Model):
    groupid = models.OneToOneField('Groups', models.DO_NOTHING, db_column='groupid', primary_key=True)  # The composite primary key (groupid, tagid) found, that is not supported. The first column is selected.
    tagid = models.ForeignKey('Tags', models.DO_NOTHING, db_column='tagid')

    class Meta:
        managed = False
        db_table = 'group_tags'
        unique_together = (('groupid', 'tagid'),)
        verbose_name_plural = 'GroupTags'


class Groups(models.Model):
    groupid = models.CharField(primary_key=True, max_length=10)
    grouptype = models.CharField(max_length=255, blank=True, null=True)
    joinrequests = models.BigIntegerField(blank=True, null=True)
    groupname = models.CharField(max_length=255)
    members = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'groups'
        verbose_name_plural = 'Groups'


class Images(models.Model):
    pageid = models.ForeignKey('Pages', models.DO_NOTHING, db_column='pageid', blank=True, null=True)
    postid = models.ForeignKey('Posts', models.DO_NOTHING, db_column='postid', blank=True, null=True)
    imageid = models.CharField(primary_key=True, max_length=10)
    imagelocation = models.CharField(max_length=255, blank=True, null=True)
    imageformat = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'images'
        verbose_name_plural = 'Images'


class IndividualUsers(models.Model):
    useraccountid = models.OneToOneField(Accounts, models.DO_NOTHING, db_column='useraccountid', primary_key=True)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    gender = models.CharField(max_length=2, blank=True, null=True)
    usertype = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'individual_users'
        verbose_name_plural = 'IndividualUsers'


class Interview(models.Model):
    employerid = models.OneToOneField(IndividualUsers, models.DO_NOTHING, db_column='employerid', primary_key=True)  # The composite primary key (employerid, jobseekerid) found, that is not supported. The first column is selected.
    jobseekerid = models.ForeignKey(IndividualUsers, models.DO_NOTHING, db_column='jobseekerid', related_name='interview_jobseekerid_set')

    class Meta:
        managed = False
        db_table = 'interview'
        unique_together = (('employerid', 'jobseekerid'),)
        verbose_name_plural = 'Interview'


class InvoiceOrders(models.Model):
    invoiceid = models.CharField(primary_key=True, max_length=10)
    paymentamount = models.FloatField(blank=True, null=True)
    billingcycle = models.CharField(max_length=50, blank=True, null=True)
    submodelid = models.ForeignKey('Premium', models.DO_NOTHING, db_column='submodelid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_orders'
        verbose_name_plural = 'InvoiceOrders'


class JobSeekers(models.Model):
    jobseekerid = models.OneToOneField(IndividualUsers, models.DO_NOTHING, db_column='jobseekerid', primary_key=True)
    roleinterested = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_seekers'
        verbose_name_plural = 'JobSeekers'


class Jobs(models.Model):
    jobid = models.CharField(primary_key=True, max_length=10)
    employerid = models.ForeignKey(Employers, models.DO_NOTHING, db_column='employerid', blank=True, null=True)
    jobseekerid = models.ForeignKey(JobSeekers, models.DO_NOTHING, db_column='jobseekerid', blank=True, null=True)
    companyname = models.CharField(max_length=255, blank=True, null=True)
    jobtitle = models.CharField(max_length=255)
    jobcategory = models.CharField(max_length=20, blank=True, null=True)
    min_salary = models.FloatField(blank=True, null=True)
    max_salary = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jobs'
        verbose_name_plural = 'Jobs'


class Lessons(models.Model):
    lessonid = models.CharField(primary_key=True, max_length=10)  # The composite primary key (lessonid, courseid) found, that is not supported. The first column is selected.
    difficulty = models.CharField(max_length=50, blank=True, null=True)
    courseid = models.ForeignKey(Courses, models.DO_NOTHING, db_column='courseid')

    class Meta:
        managed = False
        db_table = 'lessons'
        unique_together = (('lessonid', 'courseid'),)
        verbose_name_plural = 'Lessons'


class Link(models.Model):
    postid = models.OneToOneField('Posts', models.DO_NOTHING, db_column='postid', primary_key=True)
    tagid = models.ForeignKey('Tags', models.DO_NOTHING, db_column='tagid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'link'
        verbose_name_plural = 'Link'


class Messages(models.Model):
    messageid = models.CharField(primary_key=True, max_length=10)
    msenderid = models.ForeignKey(IndividualUsers, models.DO_NOTHING, db_column='msenderid', blank=True, null=True)
    mreceiverid = models.ForeignKey(IndividualUsers, models.DO_NOTHING, db_column='mreceiverid', related_name='messages_mreceiverid_set', blank=True, null=True)
    msgtimestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'messages'
        verbose_name_plural = 'Messages'


class Organizations(models.Model):
    organizationid = models.CharField(primary_key=True, max_length=10)
    organizationname = models.CharField(max_length=255, blank=True, null=True)
    organizationlocation = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'organizations'
        verbose_name_plural = 'Organizations'


class Pages(models.Model):
    pageid = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=255)
    publicationdate = models.DateField(blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True, null=True)
    pageurl = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pages'
        verbose_name_plural = 'Pages'


class Paymenttypes(models.Model):
    paymentid = models.CharField(primary_key=True, max_length=10)
    accountid = models.ForeignKey(Accounts, models.DO_NOTHING, db_column='accountid', blank=True, null=True)
    paymentname = models.CharField(max_length=50, blank=True, null=True)
    paymenttype = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paymenttypes'
        verbose_name_plural = 'Paymenttypes'


class PostComments(models.Model):
    commentid = models.CharField(primary_key=True, max_length=10)  # The composite primary key (commentid, commenttimestamp, useraccountid) found, that is not supported. The first column is selected.
    commenttimestamp = models.DateTimeField()
    useraccountid = models.ForeignKey(IndividualUsers, models.DO_NOTHING, db_column='useraccountid')
    postid = models.ForeignKey('Posts', models.DO_NOTHING, db_column='postid', blank=True, null=True)
    commentlength = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post_comments'
        unique_together = (('commentid', 'commenttimestamp', 'useraccountid'),)
        verbose_name_plural = 'PostComments'


class PostLikes(models.Model):
    useraccountid = models.OneToOneField(IndividualUsers, models.DO_NOTHING, db_column='useraccountid', primary_key=True)  # The composite primary key (useraccountid, postid) found, that is not supported. The first column is selected.
    postid = models.ForeignKey('Posts', models.DO_NOTHING, db_column='postid')
    liketype = models.CharField(max_length=255, blank=True, null=True)
    liketimestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post_likes'
        unique_together = (('useraccountid', 'postid'),)
        verbose_name_plural = 'PostLikes'


class Posts(models.Model):
    postid = models.CharField(primary_key=True, max_length=10)
    location = models.CharField(max_length=255, blank=True, null=True)
    pagepostedid = models.ForeignKey(Pages, models.DO_NOTHING, db_column='pagepostedid', blank=True, null=True)
    posttimestamp = models.DateTimeField(blank=True, null=True)
    visibility = models.CharField(max_length=255, blank=True, null=True)
    posttype = models.CharField(max_length=255, blank=True, null=True)
    likecount = models.BigIntegerField(blank=True, null=True)
    sharecount = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'posts'
        verbose_name_plural = 'Posts'


class Premium(models.Model):
    submodelid = models.OneToOneField('Subscriptiontype', models.DO_NOTHING, db_column='submodelid', primary_key=True)
    subscriptiontype = models.CharField(max_length=50, blank=True, null=True)
    billingdate = models.DateField(blank=True, null=True)
    startdate = models.DateField(blank=True, null=True)
    enddate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'premium'
        verbose_name_plural = 'Premium'


class Quizzes(models.Model):
    quizid = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=100)
    passingscore = models.FloatField(blank=True, null=True)
    certificateid = models.ForeignKey(Certificates, models.DO_NOTHING, db_column='certificateid', blank=True, null=True)
    questions = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quizzes'
        verbose_name_plural = 'Quizzes'


class Reactions(models.Model):
    reactiontypeid = models.CharField(primary_key=True, max_length=10)
    reactionname = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reactions'
        verbose_name_plural = 'Reactions'


class ReactsTo(models.Model):
    messageid = models.OneToOneField(Messages, models.DO_NOTHING, db_column='messageid', primary_key=True)  # The composite primary key (messageid, reactiontypeid) found, that is not supported. The first column is selected.
    reactiontypeid = models.ForeignKey(Reactions, models.DO_NOTHING, db_column='reactiontypeid')

    class Meta:
        managed = False
        db_table = 'reacts_to'
        unique_together = (('messageid', 'reactiontypeid'),)
        verbose_name_plural = 'ReactsTo'


class Results(models.Model):
    resultid = models.CharField(primary_key=True, max_length=10)
    certificateid = models.ForeignKey(Certificates, models.DO_NOTHING, db_column='certificateid', blank=True, null=True)
    useraccountid = models.ForeignKey(IndividualUsers, models.DO_NOTHING, db_column='useraccountid', blank=True, null=True)
    takes = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'results'
        verbose_name_plural = 'Results'


class Scores(models.Model):
    attemptid = models.CharField(max_length=10)
    useraccountid = models.OneToOneField(IndividualUsers, models.DO_NOTHING, db_column='useraccountid', primary_key=True)  # The composite primary key (useraccountid, attemptid, quizid) found, that is not supported. The first column is selected.
    quizid = models.ForeignKey(Quizzes, models.DO_NOTHING, db_column='quizid')
    name = models.CharField(max_length=100, blank=True, null=True)
    score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scores'
        unique_together = (('useraccountid', 'attemptid', 'quizid'),)
        verbose_name_plural = 'Scores'


class SettingDetails(models.Model):
    accountid = models.OneToOneField(Accounts, models.DO_NOTHING, db_column='accountid', primary_key=True)  # The composite primary key (accountid, settingid, timechanged) found, that is not supported. The first column is selected.
    settingid = models.ForeignKey('Settings', models.DO_NOTHING, db_column='settingid')
    timechanged = models.DateTimeField()
    settingchanged = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'setting_details'
        unique_together = (('accountid', 'settingid', 'timechanged'),)
        verbose_name_plural = 'SettingDetails'


class Settings(models.Model):
    settingid = models.CharField(primary_key=True, max_length=10)
    accountid = models.ForeignKey(Accounts, models.DO_NOTHING, db_column='accountid', blank=True, null=True)
    settingname = models.CharField(max_length=255, blank=True, null=True)
    settingdesc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'settings'
        verbose_name_plural = 'Settings'


class Subscriptiontype(models.Model):
    submodelid = models.CharField(primary_key=True, max_length=10)
    subscriptiontype = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscriptiontype'
        verbose_name_plural = 'Subscriptiontype'


class Tags(models.Model):
    tagid = models.CharField(primary_key=True, max_length=10)
    tagname = models.CharField(unique=True, max_length=255, blank=True, null=True)
    tagtype = models.CharField(max_length=255, blank=True, null=True)
    tagdesc = models.CharField(max_length=255, blank=True, null=True)
    tagtimestamp = models.DateTimeField(blank=True, null=True)
    tagcategory = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tags'
        verbose_name_plural = 'Tags'


class Teach(models.Model):
    certificateid = models.ForeignKey(Certificates, models.DO_NOTHING, db_column='certificateid')
    teacherid = models.OneToOneField('Teachers', models.DO_NOTHING, db_column='teacherid', primary_key=True)  # The composite primary key (teacherid, certificateid) found, that is not supported. The first column is selected.

    class Meta:
        managed = False
        db_table = 'teach'
        unique_together = (('teacherid', 'certificateid'),)
        verbose_name_plural = 'Teach'


class TeacherExpertise(models.Model):
    teacherid = models.OneToOneField('Teachers', models.DO_NOTHING, db_column='teacherid', primary_key=True)  # The composite primary key (teacherid, expertise) found, that is not supported. The first column is selected.
    expertise = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'teacher_expertise'
        unique_together = (('teacherid', 'expertise'),)
        verbose_name_plural = 'TeacherExpertise'


class Teachers(models.Model):
    teacherid = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=500, blank=True, null=True)
    certificateid = models.ForeignKey(Certificates, models.DO_NOTHING, db_column='certificateid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teachers'
        verbose_name_plural = 'Teachers'


class Text(models.Model):
    messageid = models.OneToOneField(Messages, models.DO_NOTHING, db_column='messageid', primary_key=True)
    msgtext = models.CharField(max_length=255, blank=True, null=True)
    tstatus = models.CharField(max_length=255, blank=True, null=True)
    multimediamessage = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'text'
        verbose_name_plural = 'Text'


class Uploads(models.Model):
    pageid = models.ForeignKey(Pages, models.DO_NOTHING, db_column='pageid', blank=True, null=True)
    uploadid = models.CharField(primary_key=True, max_length=10)
    timestamp = models.DateTimeField(blank=True, null=True)
    uploadformat = models.CharField(max_length=255, blank=True, null=True)
    uploadlocation = models.CharField(max_length=255, blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uploads'
        verbose_name_plural = 'Uploads'


class ViewsCount(models.Model):
    viewedaccountid = models.OneToOneField(IndividualUsers, models.DO_NOTHING, db_column='viewedaccountid', primary_key=True)  # The composite primary key (viewedaccountid, vieweraccountid, vctimestamp) found, that is not supported. The first column is selected.
    vieweraccountid = models.ForeignKey(IndividualUsers, models.DO_NOTHING, db_column='vieweraccountid', related_name='viewscount_vieweraccountid_set')
    viewtype = models.CharField(max_length=255, blank=True, null=True)
    vctimestamp = models.DateTimeField()
    vname = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'views_count'
        unique_together = (('viewedaccountid', 'vieweraccountid', 'vctimestamp'),)
        verbose_name_plural = 'ViewsCount'
