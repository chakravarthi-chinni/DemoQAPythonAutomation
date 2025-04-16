from featurefiles.steps.step_implementation_file import DemoQAStepImplementation
from BaseFile.basefile import BaseFile

from BaseFile.basefile2 import Basefileclario


def before_all(context):
    context.base=BaseFile()
#     context.clario=Basefileclario()
#
# def before_scenario(context,scenario):
#     context.impl=DemoQAStepImplementation()