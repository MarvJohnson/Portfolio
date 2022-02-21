import Client from './';

export const getBlogPosts = async () => {
  try {
    const res = await Client.get('posts/');

    return res.data;
  } catch (e) {
    console.error('Error occured when attempting to get all Blog Posts.', e);
  }
};

export const getBlogPostDetail = async (blogPostId) => {
  try {
    const res = await Client.get(`posts/${blogPostId}`);

    return res.data;
  } catch (e) {
    console.error(
      'Error occured when attempting to get details of a Blog Post',
      e
    );
  }
};
