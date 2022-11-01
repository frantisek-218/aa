from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface

from . import appbuilder, db
from .models import Osoba


class OsobaView(ModelView):
    datamodel = SQLAInterface(Osoba)

    list_columns = ["jmeno", "prijmeni", "datum", "datum_vlozeni"]
    """show_template = "appbuilder/general/model/show_cascade.html"""

db.create_all()

appbuilder.add_view(
    OsobaView, "Osoby", icon="fa-folder-open-o"
)