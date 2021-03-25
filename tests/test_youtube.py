def test_api_youtube(app, client, monkeypatch):
    """
    Test con key de youtube
    """
    res = client.get('/lista?search=test')
    assert res.status_code == 200



