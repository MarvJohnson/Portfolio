import Client from './';

export const getBlogPosts = async () => {
  try {
    const res = await Client.get('posts/');

    return res.data;
  } catch (e) {
    console.error('Error occured when attempting to get all Blog Posts.', e);
  }
};
