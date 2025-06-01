from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.


def Home(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request, 'index.html')


def About(request):
    return render(request, 'about.html')


def Contact(request):
    return render(request, 'contact.html')


def Login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']

        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'login.html', d)


def Logout(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')


def Add_Enquiry(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        c = request.POST['contact']
        e = request.POST['emailid']
        a = request.POST['age']
        g = request.POST['gender']
        try:
            Enquiry.objects.create(
                name=n, contact=c, emailid=e, age=a, gender=g)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_enquiry.html', d)


def View_Enquiry(request):
    enq = Enquiry.objects.all()
    d = {'enq': enq}
    return render(request, 'view_enquiry.html', d)
def Delete_Enquiry(request,pid):
    enquiry = Enquiry.objects.get(id=pid)
    enquiry.delete()
    return redirect('view_enquiry')


def Add_Equipment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        p = request.POST['price']
        u = request.POST['unit']
        d = request.POST['date']
        desc = request.POST['desc']
        try:
            Equipment.objects.create( name=n, price=p, unit=u, date=d, description=desc)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_equipment.html', d)


def View_Equipment(request):
    equ = Equipment.objects.all()
    d = {'equ': equ}
    return render(request, 'view_equipment.html', d)

def Delete_Equipment(request,pid):
    equipment = Equipment.objects.get(id=pid)
    equipment.delete()
    return redirect('view_equipment')

def Add_Plan(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        a = request.POST['amount']
        d = request.POST['duration']
        try:
            Plan.objects.create( name=n, amount=a, duration=d)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_plan.html', d)


def View_Plan(request):
    pln = Plan.objects.all()
    d = {'pln': pln}
    return render(request, 'view_plan.html', d)

def Delete_Plan(request,pid):
    plan = Plan.objects.get(id=pid)
    plan.delete()
    return redirect('view_plan')

def Add_Member(request):
    error = ""
    plan1 = Plan.objects.all()
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        c = request.POST['contact']
        e = request.POST['emailid']
        a = request.POST['age']
        g = request.POST['gender']
        p = request.POST['plan']
        joindate = request.POST['joindate']
        expiredate = request.POST['expdate']
        initialamount = request.POST['initialamount']
        plan = Plan.objects.filter(name=p).first()
        try:
            Member.objects.create( name=n, contact=c,emailid=e, age=a,gender=g,plan=plan, joindate=joindate, expiredate = expiredate, initialamount = initialamount)
            error = "no"
        except:
            error = "yes"
    d = {'error': error, 'plan':plan1}
    return render(request, 'add_member.html', d)


def View_Member(request):
    member = Member.objects.all()
    d = {'member': member}
    return render(request, 'view_member.html', d)

def Delete_Member(request,pid):
    member = Member.objects.get(id=pid)
    member.delete()
    return redirect('view_member')

# ---- Add these at the bottom ----

# Payment views
@login_required
def payment_history(request):
    payments = Payment.objects.filter(user=request.user).order_by('-payment_date')
    return render(request, 'payment_history.html', {'payments': payments})

@login_required
def make_payment(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        payment_method = request.POST.get('payment_method')
        Payment.objects.create(
            user=request.user,
            amount=amount,
            payment_method=payment_method,
            status='paid'
        )
        return redirect('payment_history')
    return render(request, 'make_payment.html')


# Diet Plan views
@login_required
def view_diet_plan(request):
    diet_plans = DietPlan.objects.filter(user=request.user)
    return render(request, 'diet_plans.html', {'diet_plans': diet_plans})

@login_required
def add_diet_plan(request):
    if request.method == 'POST':
        plan_name = request.POST.get('plan_name')
        description = request.POST.get('description')
        DietPlan.objects.create(
            user=request.user,
            plan_name=plan_name,
            description=description
        )
        return redirect('view_diet_plan')
    return render(request, 'add_diet_plan.html')