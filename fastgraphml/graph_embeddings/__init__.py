def get_dmgi_model():
    from .models.dmgi import DMGI
    return DMGI

def get_gat_model():
    from .models.gat import GAT
    return GAT

def get_sage_model():
    from .models.graph_sage import SAGE
    return SAGE

def get_metapath2vec_model():
    from .models.metapath2vec import METAPATH2VEC
    return METAPATH2VEC

__all__ = ["get_dmgi_model", "get_gat_model", "get_sage_model", "get_metapath2vec_model"]

