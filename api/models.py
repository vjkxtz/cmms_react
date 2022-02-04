from django.db import models

# Create your models here.

class Line(models.Model):
    line = models.CharField(max_length=15)

    def __str__(self):
        return str(self.line)

class Part(models.Model):
    assembly = models.CharField(max_length=15)

    def __str__(self):
        return str(self.assembly)

class Spare(models.Model):
    STATUS_CURRENT = (('ordered', 'Ordered'), ('po pending', 'Po Pending'), ('available', 'Available'))

    part = models.ForeignKey(Part, default='conveyor', on_delete=models.SET_DEFAULT)
    item = models.CharField(max_length=15)
    quantity = models.IntegerField()
    status = models.CharField(max_length=15, choices=STATUS_CURRENT, default='available')
    date = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return str(self.item)

class Sub_Assembly(models.Model):
    part = models.ForeignKey(Part, default='conveyor', on_delete=models.SET_DEFAULT)
    component_item = models.CharField(max_length=15)

    def __str__(self):
        return str(self.component_item)

class LineData(models.Model):
    line = models.ForeignKey(Line, default='12m', on_delete=models.SET_DEFAULT)
    part = models.ForeignKey(Part, default='conveyor', on_delete=models.SET_DEFAULT)
    sub_assembly = models.ForeignKey(Sub_Assembly, default='carrier', on_delete=models.SET_DEFAULT)
    spare = models.ForeignKey(Spare,default=1, on_delete=models.SET_DEFAULT, blank=True, null=True)
    workdone = models.CharField(max_length=150)
    date = models.DateField()
    created_on = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return (str(self.line) + " " + str(self.workdone))

