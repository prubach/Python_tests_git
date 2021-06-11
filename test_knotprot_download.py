from knotprot_download import get_proteins


def test_get_proteins():
    proteins = get_proteins()
    assert len(proteins) >= 1212

