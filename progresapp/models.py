from django.db import models

# Create your models here.


class Wilayah(models.Model):
    nmwilayah = models.CharField(max_length=60)

    def __str__(self):
        return self.nmwilayah


class Balai(models.Model):
    nmbalai = models.CharField(max_length=60)
    wilayah = models.ForeignKey(Wilayah,
                                on_delete=models.DO_NOTHING,
                                null=True)

    def __str__(self):
        return self.nmbalai


class Satker(models.Model):
    kdatker = models.CharField(max_length=8, unique=True)
    nmsatker = models.CharField(max_length=200)
    phone = models.CharField(max_length=12, null=True)
    balai = models.ForeignKey(Balai, on_delete=models.DO_NOTHING, null=True)
    # wilayah = models.CharField(max_length=25, null=True, choices=WILAYAH)
    wilayah = models.ForeignKey(Wilayah,
                                on_delete=models.DO_NOTHING,
                                null=True)

    def __str__(self):
        return self.nmsatker


class Ppk(models.Model):
    # WILAYAH = (('Wilayah I', 'Wilayah I'), ('Wilayah II', 'Wilayah II'),
    #            ('Wilayah III', 'Wilayah III'))
    nmppk = models.CharField(max_length=100)
    nmjabatan = models.CharField(max_length=100)
    phone = models.CharField(max_length=12, null=True)
    # kdsatker = models.CharField(max_length=8, null=True)
    kdsatker = models.ForeignKey(Satker,
                                 on_delete=models.DO_NOTHING,
                                 null=True)
    balai = models.ForeignKey(Balai, on_delete=models.DO_NOTHING, null=True)
    wilayah = models.ForeignKey(Wilayah,
                                on_delete=models.DO_NOTHING,
                                null=True)

    def __str__(self):
        return self.nmppk


class Satoutput(models.Model):
    nmsatoutput = models.CharField(max_length=45)

    def __str__(self):
        return self.nmsatoutput


class Satoutcome(models.Model):
    nmsatoutcome = models.CharField(max_length=45)

    def __str__(self):
        return self.nmsatoutcome


class Ta(models.Model):
    tahun = models.CharField(max_length=45)

    def __str__(self):
        return self.tahun


class Ks(models.Model):
    nmks = models.CharField(max_length=45)

    def __str__(self):
        return self.nmks


class Fnf(models.Model):
    nmfnf = models.CharField(max_length=45)

    def __str__(self):
        return self.nmfnf


class Sycmyc(models.Model):
    nmsycmyc = models.CharField(max_length=45)

    def __str__(self):
        return self.nmsycmyc


class Kodeoutput(models.Model):
    kdoutput = models.CharField(max_length=3, unique=True)
    nmkdoutput = models.CharField(max_length=250)

    def __str__(self):
        return self.nmkdoutput


class Tag(models.Model):
    tag = models.CharField(max_length=45, null=True)

    def __str__(self):
        return self.tag


class Sumberdana(models.Model):
    sumberdana = models.CharField(max_length=45, null=True)

    def __str__(self):
        return self.sumberdana


class Paket(models.Model):
    # WILAYAH = (('Wilayah I', 'Wilayah I'), ('Wilayah II', 'Wilayah II'),
    #            ('Wilayah III', 'Wilayah III'))
    # KS = (('K', 'K'), ('S', 'S'), ('Administrasi', 'Administrasi'))
    # TA = (('Stock', 'Stock'), ('Baseline', 'Baseline'), ('2021', '2021'),
    #       ('2020', '2020'))
    # FNF = (('F', 'F'), ('NF', 'NF'), ('AP', 'AP'))
    # SYCMYC = (('SYC', 'SYC'), ('MYC', 'MYC'), ('MYC Lanjutan', 'MYC Lanjutan'))
    # SATOUTPUT = (('Dokumen', 'Dokumen'), ('Titik', 'Titik'), ('Buah', 'Buah'),
    #              ('Km', 'Km'), ('Ha', 'Ha'), ('Layanan', 'Layanan'))
    # SATOUTCOME = (('m3/dtk', 'm3/dtk'), ('Dokumen', 'Dokumen'),
    #               ('Titik', 'Titik'), ('Buah', 'Buah'), ('Km', 'Km'),
    #               ('Ha', 'Ha'), ('Layanan', 'Layanan'))

    balai = models.ForeignKey(Balai, on_delete=models.DO_NOTHING, null=True)
    nmgiat = models.CharField(max_length=4)
    nmpaket = models.CharField(max_length=250)
    kdoutput = models.ForeignKey(Kodeoutput,
                                 on_delete=models.DO_NOTHING,
                                 null=True)
    # kdoutput = models.CharField(max_length=3)
    # kdoutput_link = models.ForeignKey(Kodeoutput,
    #                                   on_delete=models.DO_NOTHING,
    #                                   null=True)
    # kdpaket = models.CharField(max_length=10)
    pagurmp = models.FloatField(null=True)
    trgoutput = models.DecimalField(max_digits=10, decimal_places=3)
    satoutput = models.ForeignKey(Satoutput,
                                  on_delete=models.DO_NOTHING,
                                  null=True)
    trgoutcome = models.DecimalField(max_digits=10, decimal_places=3)
    satoutcome = models.ForeignKey(Satoutcome,
                                   on_delete=models.DO_NOTHING,
                                   null=True)
    ta = models.ForeignKey(Ta, on_delete=models.DO_NOTHING, null=True)
    ppk = models.ForeignKey(Ppk, on_delete=models.DO_NOTHING, null=True)
    ks = models.ForeignKey(Ks, on_delete=models.DO_NOTHING, null=True)
    fnf = models.ForeignKey(Fnf, on_delete=models.DO_NOTHING, null=True)
    sycmyc = models.ForeignKey(Sycmyc, on_delete=models.DO_NOTHING, null=True)
    tag = models.ManyToManyField(Tag)
    sumberdana = models.ManyToManyField(Sumberdana)
    # kdoutput = models.ForeignKey(Kodeoutput,related_name='kdoutput_set' on_delete=models.DO_NOTHING, null=True)
    satker = models.ForeignKey(Satker, on_delete=models.DO_NOTHING, null=True)
    # satker = models.CharField(max_length=8)
    # satker_link = models.ForeignKey(Satker,
    #                                 on_delete=models.DO_NOTHING,
    #                                 null=True)
    wilayah = models.ForeignKey(Wilayah,
                                on_delete=models.DO_NOTHING,
                                null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.nmpaket