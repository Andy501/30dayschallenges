def domain_name(url):
    #re can handle better
    
    #if header http or https header is presented
    if len(urlparse(url).scheme) >= 1:
        if 'www.' in url:
            t = ((urlparse(url).netloc))
            reducedURL = ('.'.join(t.split('.')[1:2]))
            
        else:
            t = ((urlparse(url).netloc))
            reducedURL = ('.'.join(t.split('.')[0:1]))
    else:
        t = ((urlparse(url).path))
        reducedURL = ('.'.join(t.split('.')[1:2]))
    return reducedURL

    ####missing hypen pass
    