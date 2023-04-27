from rest_framework.renderers import BrowsableAPIRenderer, TemplateHTMLRenderer


class TableHtmlRenderer(TemplateHTMLRenderer):
    media_type = 'text/html'
    format = 'api'
    template_name = 'csv_api/csvtask_download.html'

    def get_template_context(self, data, renderer_context):
        context = {'data': data}
        response = renderer_context['response']
        if response.exception:
            context['status_code'] = response.status_code
        return context


class CustomRenderer(BrowsableAPIRenderer):

    def get_default_renderer(self, view):

        return TableHtmlRenderer()
