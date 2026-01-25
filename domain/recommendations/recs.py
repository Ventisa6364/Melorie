from data.models.models_posts import Post

def get_recomended_posts(post, limit=10):
    recs = list(Post.objects.filter(category=post.category).exclude(id=post.id).order_by('-published_at')[:limit])

    if len(recs) < limit:
        extra = Post.objects.exclude(id=post.id).order_by('-id')[:limit]  
        for el in extra:
            if el not in recs: 
                recs.append(el)

    return recs[:limit]