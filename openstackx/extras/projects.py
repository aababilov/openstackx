import base64
from openstackx.api import base


class ProjectManager(base.Manager):
    def zipfile(self, project_id):
        resp, body = self.api.connection.get("/extras/projects/%s/zipfile" % project_id)
        return base64.b64decode(body["zipfile"])
