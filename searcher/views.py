from fastapi import APIRouter
from fastapi.responses import JSONResponse
from searcher.smart_search import find_n_docs, get_docs_from_db
from searcher.delete_post import deletion
from generator.generator import generate
from db.db import posts
from config import elastic_index, elastic_host, max_posts_count
from modules.models import PostModel


search_router = APIRouter()


@search_router.post('/search/', response_class=JSONResponse)
async def search_by_text(post: PostModel):
    data = find_n_docs(elastic_host, elastic_index, max_posts_count, post.text)
    return get_docs_from_db(posts, data)


@search_router.delete('/delete_post/{id}', response_class=JSONResponse)
async def delete_post(id):
    return deletion(elastic_host, elastic_index, posts, id)


@search_router.patch('/generate/', response_class=JSONResponse)
async def generate_data():
    return generate('posts.csv', posts)
