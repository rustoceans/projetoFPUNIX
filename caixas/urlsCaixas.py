from django.conf.urls import patterns, include, url


urlpatterns = patterns('caixas.views',
    url(r'^adicionar/$', 'caixaAdicionar'),
    url(r'^editar/(?P<pk>\d+)/$', 'caixaEditar'),
    url(r'^salvar/$', 'caixaSalvar'),
    url(r'^excluir/(?P<pk>\d+)/$', 'caixaExcluir'),
    url(r'^pesquisar/$', 'caixaPesquisar'),
    url(r'^$', 'caixaListar'),
)