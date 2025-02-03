from featurefiles.steps.step_implementation_file import DemoQAStepImplementation
from BaseFile.basefile import BaseFile


def before_all(context):
    context.base=BaseFile()
    print(f"DEBUG: context.base type -> {type(context.base)}") 
    print(f"DEBUG: context.base.driver type -> {type(context.base.driver)}")