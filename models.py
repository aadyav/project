from django.db import models



class village(models.Model):
    family_statistics = models.CharField(max_length = 250)
    health = models.CharField(max_length = 250)
    education = models.CharField(max_length = 250)
    livelihood = models.CharField(max_length = 250)


class family_stats(models.Model):
    village = models.ForeignKey(village, on_delete=models.CASCADE)
    file_type = models.CharField(max_length = 10)
    family_head =  models.CharField(max_length = 250)
    
