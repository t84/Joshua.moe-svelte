<script>
  import { page } from '$app/stores';
</script>

<nav class="navbar justify-center">
  <a href="/" class={$page.url.pathname === '/' ? 'active' : ''}>Home</a>
  <a href="/blog" class={$page.url.pathname === '/blog' ? 'active' : ''}>Blog</a>
  <a href="/friends" class={$page.url.pathname === '/friends' ? 'active' : ''}>Friends</a>
  <a href="/guestbook" class={$page.url.pathname === '/guestbook' ? 'active' : ''}>Guestbook</a>
</nav>

<style>
  .navbar {
    display: flex;
    gap: 1rem;
    padding: 1rem;
    background: #181818;
    border-bottom: 2px solid white; 
  }
  a {
    text-decoration: none;
    color: #f8f8f8;
  }
  .active {
    font-weight: bold;
    border-bottom: 2px solid #f8f8f8; 
  }
</style>
