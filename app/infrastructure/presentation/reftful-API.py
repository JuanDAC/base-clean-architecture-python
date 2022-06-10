

from app.infrastructure.presentation.interface import PresentationManager
from app.application.userManager import UserManager


class API(PresentationManager): 

    def get_idetification():

        identificationRaw = UserManager.obtainIdetification()

        identificationparsed = identificationRaw

        return identificationparsed
        

