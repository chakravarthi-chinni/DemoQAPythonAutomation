from featurefiles.steps.step_implementation_file import DemoQAStepImplementation
from BaseFile.basefile import BaseFile


def before_all(context):
    context.base=BaseFile()