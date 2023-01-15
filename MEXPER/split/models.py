from django.db import models
from django.db.models import Sum

VAR_COSTS = [('WATBILL','Water Bill'), ('ElECBILL', 'Electricity Bill')]
FIX_COSTS =[('RENT','Rent'), ('DEBT','Debt'), ('SUBS', 'Subscriptions')]
PRIORITY = [('H','High'),('M','Medium'),('L','Low')]
PAID = [('Y','Yes'),('N','No')]


class Amount(models.Model):
    amount = models.FloatField('Amount')
    inc_date = models.DateField(null=True)
    def __str__(self):
        return self.amount
    class Meta:
        db_table = 'amount'

class Fixed(models.Model):
    f_choice = models.CharField('Payment',max_length=200,choices=FIX_COSTS)
    cost = models.FloatField('Cost')
    due_date=models.DateTimeField('Due Date')
    status = models.CharField('Paid?',max_length=3, choices=PAID)
    class Meta:
        ordering = ['due_date']
    def __str__(self):
        return self.f_choice 



class Variable(models.Model):
    v_choice = models.CharField('Payment',max_length=200,choices=VAR_COSTS)
    cost = models.FloatField('Cost')
    due_date=models.DateTimeField('Due Date')
    status = models.CharField('Paid?',max_length=3, choices=PAID)
    class Meta:
        ordering = ['due_date']
    def __str__(self):
        return self.v_choice
    
class Saving(models.Model):
    saving = models.FloatField('Saving Amount:')
    class Meta:
        ordering = ['due_date']
    def __str__(self):
        return self.saving
      
class events(models.Model):
    name=models.CharField(max_length=200)
    event_date=models.DateTimeField('Event Date')
    cost= models.FloatField(default=0)
    status = models.CharField(max_length=3, choices=PAID)
    priority = models.CharField(max_length=1, choices=PRIORITY)
    class Meta:
        ordering = ['event_date']
    def __str__(self):
        return self.name

class Alls(models.Model):
    Fost = models.ForeignKey(Fixed, on_delete= models.DO_NOTHING)
    Vost = models.ForeignKey(Variable, on_delete= models.DO_NOTHING)
    eost = models.ForeignKey(events, on_delete= models.DO_NOTHING)


f= Fixed.objects.annotate(sum=Sum("cost"))
v= Fixed.objects.annotate(sum=Sum("cost"))
e= Fixed.objects.annotate(sum=Sum("cost"))


def net():
    net_inc = Amount.amount - (e + Saving.saving + v + f)
    return net_inc 


