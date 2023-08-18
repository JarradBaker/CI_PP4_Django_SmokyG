from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Blog, Comment, Booking
from .forms import CommentForm, BookingForm


# Create your views here.
def blog(request):
    blogs = Blog.objects.filter(status="Published")
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog.html', context)


class BlogPost(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Blog.objects.filter(status="Published")
        blog = get_object_or_404(queryset, slug=slug)
        comments = blog.comments.filter(approved=True).order_by(created_on)
        liked = False
        if blog.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "blog": blog,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Blog.objects.filter(status="Published")
        blog = get_object_or_404(queryset, slug=slug)
        comments = blog.comments.filter(approved=True).order_by('created_on')
        liked = False
        if blog.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.blog = blog
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "blog": blog,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": comment_form
            },
        )


class PostLike(View):
    def post(self, request, slug):
        post = get_object_or_404(Blog, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def delete_comment(request, slug, comment_id):
    blog = get_object_or_404(Blog, slug=slug)
    comment = get_object_or_404(Comment, id=comment_id, blog=blog)

    if request.method == 'POST':
        comment.delete()
        # You can add a success message or any other logic here
        return redirect('post_detail', slug=slug)  # Redirect to the post's detail view

    return render(request, 'comment_confirm_delete.html', {'comment': comment})


def edit_comment(request, slug, comment_id):
    blog = get_object_or_404(Blog, slug=slug)
    comment = get_object_or_404(Comment, id=comment_id, blog=blog)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form.save()
            # You can add a success message or any other logic here
            return redirect('post_detail', slug=slug)  # Redirect to the post's detail view
    else:
        comment_form = CommentForm(instance=comment)

    return render(request, 'edit_comment.html', {'comment_form': comment_form, 'comment': comment})


def create_booking(request):
    if request.method == 'POST':
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('bookings')
    else:
        booking_form = BookingForm()
    return render(request, 'create_booking.html', {'booking_form': booking_form})


def booking_list(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking_list.html', {'bookings': bookings})


def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        booking_form = BookingForm(request.POST, instance=booking)
        if booking_form.is_valid():
            booking_form.save()
            return redirect('bookings')
    else:
        booking_form = BookingForm(instance=booking)
    return render(request, 'edit_booking.html', {'booking_form': booking_form, 'booking': booking})


def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        booking.delete()
        return redirect('bookings')
    return render(request, 'delete_booking.html', {'booking': booking})

# def show_post(request, slug, )


# class PostList(generic.ListView):
#     model = Post
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'index.html'
#     paginate_by = 6


# class PostDetail(View):

#     def get(self, request, slug, *args, **kwargs):
#         queryset = Post.objects.filter(status=1)
#         post = get_object_or_404(queryset, slug=slug)
#         comments = post.comments.filter(approved=True).order_by('created_on')
#         liked = False
#         if post.likes.filter(id=self.request.user.id).exists():
#             liked = True

#         return render(
#             request,
#             "post_detail.html",
#             {
#                 "post": post,
#                 "comments": comments,
#                 "commented": False,
#                 "liked": liked,
#                 "comment_form": CommentForm()
#             },
#         )

#     def post(self, request, slug, *args, **kwargs):
#         queryset = Post.objects.filter(status=1)
#         post = get_object_or_404(queryset, slug=slug)
#         comments = post.comments.filter(approved=True).order_by('created_on')
#         liked = False
#         if post.likes.filter(id=self.request.user.id).exists():
#             liked = True

#         comment_form = CommentForm(data=request.POST)

#         if comment_form.is_valid():
#             comment_form.instance.email = request.user.email
#             comment_form.instance.name = request.user.username
#             comment = comment_form.save(commit=False)
#             comment.post = post
#             comment.save()
#         else:
#             comment_form = CommentForm()

#         return render(
#             request,
#             "post_detail.html",
#             {
#                 "post": post,
#                 "comments": comments,
#                 "commented": True,
#                 "liked": liked,
#                 "comment_form": CommentForm()
#             },
#         )
