from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

from Verfahrensverzeichnis.admin import user_admin_site

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Oos_Abschlussprojekt.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', RedirectView.as_view(url=reverse_lazy('user_admin_site:Verfahrensverzeichnis_verfahrensverzeichnis_change', args=(1,))), name="index"),
    url(r'^objects/', include(user_admin_site.urls), name='user_admin_site'),
    url(r'^report$', 'PDF_Generator.views.report', name='report'),
    url(r'^report_html$', 'PDF_Generator.views.report_pdf', name='report_html'),
)
