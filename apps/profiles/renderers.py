import json

from rest_framework.renderers import JSONRenderer

class ProfileJSONRenderer(JSONRenderer):
    """
        Custom render model to have profile namespace for the error renders
    """
    charset = 'utf-8'

    def render(self, data, accepted_media_types=None, renderer_context=None):
        errors = data.get('errors', None)

        if errors is not None:
            return super(ProfileJSONRender, self).render(data)
        
        return json.dumps({"profile": data})