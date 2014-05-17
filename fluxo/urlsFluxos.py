from django.conf.urls import patterns, include, url


urlpatterns = patterns('fluxo.views',
    url(r'^adicionar/$', 'fluxoAdicionar'),
    url(r'^editar/(?P<pk>\d+)/$', 'fluxoEditar'),
    url(r'^salvar/$', 'fluxoSalvar'),
    url(r'^excluir/(?P<pk>\d+)/$', 'fluxoExcluir'),
    url(r'^pesquisar/$', 'fluxoPesquisar'),
    url(r'^$', 'fluxoListar'),
)

