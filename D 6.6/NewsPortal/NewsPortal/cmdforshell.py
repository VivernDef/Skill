
User.objects.create_user('tester1')
User.objects.create_user('tester2')
User.objects.create_user('tester3')


Author.objects.create (pk = "1", rate = 0.0)
Author.objects.create (pk = "2", rate = 3.0)
Author.objects.create (pk = "3", rate = 0.0)


Category.objects.create(theme = 'Новости Утра')
Category.objects.create(theme = 'Политика')
Category.objects.create(theme = 'Научная Фантастика')
Category.objects.create(theme = 'Природа')


a1 = Category(theme = "Природа Ночью")
a1.save()


Post.objects.create(theme_news = "Война и Мир", body_news = "Уникальным в и
стории мировой литературы является классический роман Льва Николаевича Толстого
повествующий о жизни русского общества в эпоху наполеоновских войн.", rate_news =
 0.0, authors_id = 2)


Post.objects.create(theme_news = "Миграции Дятлов", body_news = "Обычно дятлы мигрируют в более теплые базы данных, там они там они активно набирают большую популяцию объектов", ra
te_news = 0.0, authors_id = 3)


Post.objects.create(theme_news = "Обучение Дятлов", body_news = "В дикой природе популяция дятлов очень глупа и пуглива, но с каждым пройденным модулем они становятся умнее,легче а
даптирются в новой среде обитания", rate_news = 0.0, authors_id = 3)


PostCategory.objects.create(post_id = 1, category_id = 2)
PostCategory.objects.create(post_id = 1, category_id = 3)
PostCategory.objects.create(post_id = 2, category_id = 4)
PostCategory.objects.create(post_id = 3, category_id = 4)


sam_python = PostCategory(post=python, category=sam)
sam_python.save()


Comment.objects.create(post_id = 3, commenter_user_id = 1, comments = "Дайте список дятлов" )
Comment.objects.create(post_id = 2, commenter_user_id = 1, comments = "Самая популярная тема для публикаций" )
Comment.objects.create(post_id = 1, commenter_user_id = 2, comments = "Открываю новый цикл романов" )
Comment.objects.create(post_id = 1, commenter_user_id = 3, comments = "Романы уже никому не интересны" )


Post.objects.get(pk=3).preview()


Post.objects.get(pk=1).dislike()
Post.objects.get(pk=2).like()


Comment.objects.get(pk=3).like()
Comment.objects.get(pk=4).dislike()


