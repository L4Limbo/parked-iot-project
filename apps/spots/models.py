from django.db import models

class Organization(models.Model):
    orgid = models.AutoField(db_column='orgId', primary_key=True)  # Field name made lowercase.
    orgname = models.CharField(db_column='orgName', max_length=50)  # Field name made lowercase.
    address = models.CharField(max_length=50)
    building = models.BooleanField()
    buildlat = models.DecimalField(db_column='buildLat', max_digits=18, decimal_places=16, blank=True, null=True)  # Field name made lowercase.
    buildlong = models.DecimalField(db_column='buildLong', max_digits=18, decimal_places=16, blank=True, null=True)  # Field name made lowercase.
    ramp = models.BooleanField(blank=True, null=True)

class Catparking(models.Model):
    catid = models.AutoField(db_column='catId', primary_key=True)  # Field name made lowercase.
    dmslong = models.DecimalField(db_column='dmsLong', max_digits=18, decimal_places=16)  # Field name made lowercase.
    dmslat = models.DecimalField(db_column='dmsLat', max_digits=18, decimal_places=16)  # Field name made lowercase.
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    categoryparking = models.CharField(db_column='categoryParking', max_length=10)  # Field name made lowercase.
    allowedvehicletype = models.CharField(db_column='allowedVehicleType', max_length=20)  # Field name made lowercase.
    totalspotnumber = models.IntegerField(db_column='totalSpotNumber')  # Field name made lowercase.
    timemodified = models.DateTimeField(db_column='timeModified', auto_now=True)  # Field name made lowercase.
    address = models.CharField(max_length=100)
    requiredpermit = models.CharField(db_column='requiredPermit', max_length=50)  # Field name made lowercase.
    orgid = models.ForeignKey('Organization', models.DO_NOTHING, db_column='orgId')  # Field name made lowercase.

class Parkingspot(models.Model):
    spotid = models.AutoField(db_column='spotId', primary_key=True)  # Field name made lowercase.
    spotlong = models.DecimalField(db_column='spotLong', max_digits=18, decimal_places=16)  # Field name made lowercase.
    spotlat = models.DecimalField(db_column='spotLat', max_digits=18, decimal_places=16)  # Field name made lowercase.
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    categoryspot = models.CharField(db_column='categorySpot', max_length=20)  # Field name made lowercase.
    catid = models.ForeignKey('Catparking', models.DO_NOTHING, db_column='catId')  # Field name made lowercase.

class Getdata(models.Model):
    dataid = models.AutoField(db_column='dataId', primary_key=True)
    datatext = models.TextField()

class PublicUser(models.Model):
    userid = models.AutoField(db_column='userId', primary_key=True)  # Field name made lowercase.
    useremail = models.CharField(db_column='userEmail', max_length=50)  # Field name made lowercase.
    userpassword = models.CharField(db_column='userPassword', max_length=50)  # Field name made lowercase.
    usercardcode = models.CharField(db_column='userCardCode', max_length=50)  # Field name made lowercase.
    usercardimage = models.BinaryField(db_column='userCardImage')  # Field name made lowercase.