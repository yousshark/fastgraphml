def get_dmgi_model():
    from .graph_embeddings.models.dmgi import DMGI
    return DMGI

def get_gat_model():
    from .graph_embeddings.models.gat import GAT
    return GAT

def get_sage_model():
    from .graph_embeddings.models.graph_sage import SAGE
    return SAGE

def get_metapath2vec_model():
    from .graph_embeddings.models.metapath2vec import METAPATH2VEC
    return METAPATH2VEC

__all__ = ["get_dmgi_model", "get_gat_model", "get_sage_model", "get_metapath2vec_model"]

