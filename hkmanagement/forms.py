from django import forms
from .models import Admin,Asset,Task,Worker,TaskAssignment

class AssetForm(forms.ModelForm):

    class Meta:
        model = Asset
        fields = ('assetname',)

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('assetid','taskname','frequency',)

class WorkerForm(forms.ModelForm):

    class Meta:
        model = Worker
        fields = ('name',)

class TaskAllocationForm(forms.ModelForm):

    class Meta:
        model = TaskAssignment
        fields = ('assetid','taskid','workerid','timeOfAllocation','taskToBePerformedBy')

    def clean(self):
        if self.cleaned_data['timeOfAllocation'] >= self.cleaned_data['taskToBePerformedBy']:
            raise forms.ValidationError("End date cannot be less than start data")
        return self.cleaned_data