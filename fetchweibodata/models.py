from django.db import models


class WeiboData(models.Model):
    reposts_count = models.IntegerField()
    truncated = models.CharField(max_length=10)
    text = models.TextField()
    mid = models.CharField(max_length=30)
    attitudes_count = models.IntegerField()
    favorited = models.CharField(max_length=10)
    idstr = models.CharField(max_length=30)
    created_at = models.CharField(max_length=40)
    comments_count = models.IntegerField()

class WeiboUserData(models.Model):
    bi_followers_count = models.IntegerField()
    domain = models.CharField(max_length=30,blank=True,null=True)
    id = models.CharField(max_length=30,primary_key=True)
    idstr = models.CharField(max_length=30)
    city = models.IntegerField(blank=True,null=True)
    province = models.IntegerField(blank=True,null=True)
    followers_count = models.IntegerField()
    location = models.CharField(max_length=30,blank=True,null=True)
    profile_url = models.CharField(max_length=30,blank=True,null=True)
    statuses_count = models.IntegerField()
    friends_count = models.IntegerField()
    allow_all_act_msg = models.CharField(max_length=10)
    allow_all_comment = models.CharField(max_length=10)
    geo_enabled = models.CharField(max_length=10,blank=True,null=True)
    name = models.CharField(max_length=30,blank=True,null=True)
    lang = models.CharField(max_length=10,blank=True,null=True)
    favourites_count = models.IntegerField()
    screen_name = models.CharField(max_length=30,blank=True,null=True)
    gender = models.CharField(max_length=5,blank=True,null=True)
    created_at = models.CharField(max_length=40)



