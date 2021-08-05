from .models. import Post


def validate_post():
#1. bring all data
    posts = Post.objects.all()
#2. Check whether there is & in posts
    for post in posts:
        if '&' in post.content:
            print(post.id, 'there is & with the content')
#3. If there is '&' , delete the '&'
            post.content = post.content.replace('&','')
#4. Save Data
            post.save()
        if post.dt_modified < post.dt_created:
            print(post.id, 'this content modified date is wrong')
            post.save()