# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

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
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
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


class Color(models.Model):
    cbakeywordeng = models.TextField(db_column='cbaKeywordEng', blank=True, null=True)  # Field name made lowercase.
    cbag1 = models.TextField(db_column='cbaG1', blank=True, null=True)  # Field name made lowercase.
    cbaalikeword = models.TextField(db_column='cbaAlikeWord', blank=True, null=True)  # Field name made lowercase.
    cbaseq = models.TextField(db_column='cbaSeq', blank=True, null=True)  # Field name made lowercase.
    cbatyp = models.TextField(db_column='cbaTyp', blank=True, null=True)  # Field name made lowercase.
    cbar1 = models.TextField(db_column='cbaR1', blank=True, null=True)  # Field name made lowercase.
    cbakeyword = models.TextField(db_column='cbaKeyword', blank=True, null=True)  # Field name made lowercase.
    cbab1 = models.TextField(db_column='cbaB1', blank=True, null=True)  # Field name made lowercase.
    rgb = models.TextField(db_column='RGB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'color'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Likes(models.Model):
    userid = models.CharField(max_length=50)
    novel_image = models.TextField(blank=True, null=True)
    novel_title = models.TextField(blank=True, null=True)
    song_image = models.TextField(blank=True, null=True)
    song_title = models.TextField(blank=True, null=True)
    song_singer = models.TextField(blank=True, null=True)
    book_price = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'likes'


class Matchreview(models.Model):
    userid = models.CharField(max_length=50)
    rating = models.IntegerField(blank=True, null=True)
    matchreview = models.TextField(blank=True, null=True)
    booktitle = models.CharField(max_length=100, blank=True, null=True)
    timeday = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'matchreview'


class Music(models.Model):
    year = models.TextField(blank=True, null=True)
    songid = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    singer = models.TextField(blank=True, null=True)
    lyrics = models.TextField(blank=True, null=True)
    singer_id = models.TextField(blank=True, null=True)
    album_id = models.TextField(blank=True, null=True)
    album_images = models.TextField(blank=True, null=True)
    album_name = models.TextField(blank=True, null=True)
    release_date = models.TextField(blank=True, null=True)
    total_tracks = models.TextField(blank=True, null=True)
    track_pop = models.TextField(blank=True, null=True)
    track_number = models.TextField(blank=True, null=True)
    singer_popularity = models.TextField(blank=True, null=True)
    singer_followers = models.TextField(blank=True, null=True)
    singer_genres = models.TextField(blank=True, null=True)
    modification_time = models.DateTimeField()
    insertion_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'music'


class MusicAlbum(models.Model):
    singer_id = models.TextField(blank=True, null=True)
    singer_name = models.TextField(blank=True, null=True)
    album_id = models.TextField(blank=True, null=True)
    album_images = models.TextField(blank=True, null=True)
    album_name = models.TextField(blank=True, null=True)
    release_date = models.TextField(blank=True, null=True)
    total_tracks = models.TextField(blank=True, null=True)
    track_id = models.TextField(blank=True, null=True)
    track_name = models.TextField(blank=True, null=True)
    track_pop = models.TextField(blank=True, null=True)
    track_number = models.TextField(blank=True, null=True)
    modification_time = models.DateTimeField()
    insertion_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'music_album'


class MusicLyrics(models.Model):
    year = models.TextField(blank=True, null=True)
    songid = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    singer = models.TextField(blank=True, null=True)
    lyrics = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'music_lyrics'


class MusicSinger(models.Model):
    name = models.TextField(blank=True, null=True)
    popularity = models.TextField(blank=True, null=True)
    follwers = models.TextField(blank=True, null=True)
    genres = models.TextField(blank=True, null=True)
    singer_id = models.TextField(blank=True, null=True)
    images = models.TextField(blank=True, null=True)
    modification_time = models.DateTimeField()
    insertion_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'music_singer'


class Novel(models.Model):
    itemid = models.TextField(db_column='itemId', blank=True, null=True)  # Field name made lowercase.
    title = models.TextField(blank=True, null=True)
    pubdate = models.TextField(db_column='pubDate', blank=True, null=True)  # Field name made lowercase.
    coversmallurl = models.TextField(db_column='coverSmallUrl', blank=True, null=True)  # Field name made lowercase.
    coverlargeurl = models.TextField(db_column='coverLargeUrl', blank=True, null=True)  # Field name made lowercase.
    publisher = models.TextField(blank=True, null=True)
    pricestandard = models.TextField(db_column='priceStandard', blank=True, null=True)  # Field name made lowercase.
    customerreviewrank = models.TextField(db_column='customerReviewRank', blank=True, null=True)  # Field name made lowercase.
    author = models.TextField(blank=True, null=True)
    isbn = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    story = models.TextField(blank=True, null=True)
    review = models.TextField(blank=True, null=True)
    piece = models.TextField(blank=True, null=True)
    dominant_topic = models.TextField(db_column='Dominant_Topic', blank=True, null=True)  # Field name made lowercase.
    topic_keywords = models.TextField(db_column='Topic_Keywords', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'novel'


class NovelColor(models.Model):
    novel = models.TextField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'novel_color'


class NovelSing(models.Model):
    novel = models.TextField(blank=True, null=True)
    song = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'novel_sing'


class NovelStory(models.Model):
    itemid = models.TextField(db_column='itemId', blank=True, null=True)  # Field name made lowercase.
    title = models.TextField(blank=True, null=True)
    story = models.TextField(blank=True, null=True)
    review = models.TextField(blank=True, null=True)
    piece = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'novel_story'


class NovelTopic(models.Model):
    dominant_topic = models.TextField(db_column='Dominant_Topic', blank=True, null=True)  # Field name made lowercase.
    topic_keywords = models.TextField(db_column='Topic_Keywords', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'novel_topic'


class Novelnovel(models.Model):
    itemid = models.TextField(db_column='itemId', blank=True, null=True)  # Field name made lowercase.
    title = models.TextField(blank=True, null=True)
    pubdate = models.TextField(db_column='pubDate', blank=True, null=True)  # Field name made lowercase.
    coversmallurl = models.TextField(db_column='coverSmallUrl', blank=True, null=True)  # Field name made lowercase.
    coverlargeurl = models.TextField(db_column='coverLargeUrl', blank=True, null=True)  # Field name made lowercase.
    publisher = models.TextField(blank=True, null=True)
    pricestandard = models.TextField(db_column='priceStandard', blank=True, null=True)  # Field name made lowercase.
    customerreviewrank = models.TextField(db_column='customerReviewRank', blank=True, null=True)  # Field name made lowercase.
    author = models.TextField(blank=True, null=True)
    isbn = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    story = models.TextField(blank=True, null=True)
    review = models.TextField(blank=True, null=True)
    piece = models.TextField(blank=True, null=True)
    modification_time = models.DateTimeField()
    insertion_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'novelnovel'


class Review(models.Model):
    userid = models.CharField(max_length=50)
    rating = models.IntegerField(blank=True, null=True)
    review = models.TextField(blank=True, null=True)
    booktitle = models.CharField(max_length=100, blank=True, null=True)
    timeday = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review'


class Signup(models.Model):
    id = models.IntegerField(primary_key=True)
    userid = models.CharField(max_length=50)
    userpw = models.CharField(max_length=1000)
    username = models.CharField(max_length=50)
    userbirthday = models.CharField(max_length=50, blank=True, null=True)
    usergender = models.CharField(max_length=50, blank=True, null=True)
    useremail = models.CharField(max_length=200)
    userphone = models.CharField(max_length=50)
    role = models.CharField(max_length=50)

    def __str__(self):
        return str({'userid': self.userid, 'userpw': self.userpw, 'username': self.username,
                    'usergender': self.usergender, 'useremail': self.useremail,
                    'userbirthday': self.userbirthday, 'userphone': self.userphone, 'role': self.role})

    class Meta:
        managed = False
        db_table = 'signup'
