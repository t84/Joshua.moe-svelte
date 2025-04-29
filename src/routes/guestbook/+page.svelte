<script>
  import NavBar from '$lib/components/NavBar.svelte';
  import { onMount, onDestroy } from 'svelte';

  let entries = [
    {
      name: 'Joshua',
      message: 'Hey this is pretty cool!',
      timestamp: '2025-04-29T22:12:58.957Z',
      avatar: '/images/Joshua_avatar.png'
    }
  ];

  let name = '';
  let message = '';
  let error = '';
  let sending = false;
  let rateLimitError = '';
  let rateLimitRemaining = 0;
  let timerInterval;

  // if an image url isnt provided https://api.dicebear.com/7.x/thumbs/svg?seed=

  async function submitMessage() {
    if (!name || !message) {
      error = 'Name and message are required.';
      return;
    }

    sending = true;
    error = '';

    try {
      const res = await fetch('https://cors.joshua.moe/?url=https://guestbook.joshua.moe', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name, message }),
      });

      if (res.ok) {
        name = '';
        message = '';
        rateLimitRemaining = 0;
        rateLimitError = '';
      } else if (res.status === 429) {
        const text = await res.text();
        const match = text.match(/Try again in (\d+)s/);
        if (match) {
          rateLimitRemaining = parseInt(match[1], 10);
          rateLimitError = `You can send a message again in ${rateLimitRemaining} seconds.`;
          startRateLimitTimer();
        }
      } else {
        throw new Error('Failed to send message to the webhook.');
      }
    } catch (e) {
      error = e.message;
    } finally {
      sending = false;
    }
  }

  function startRateLimitTimer() {
    timerInterval = setInterval(() => {
      if (rateLimitRemaining > 0) {
        rateLimitRemaining -= 1;
        rateLimitError = `You can send a message again in ${rateLimitRemaining} seconds.`;
      } else {
        clearInterval(timerInterval);
        rateLimitError = '';
      }
    }, 1000);
  }

  onMount(() => {});

  onDestroy(() => {
    if (timerInterval) {
      clearInterval(timerInterval);
    }
  });

  function formatTimestamp(timestamp) {
    const date = new Date(timestamp);
    return date.toLocaleString();
  }
</script>

<NavBar />

<main class="p-4 max-w-2xl mx-auto space-y-6">
  <h1 class="text-3xl">📖 Guestbook</h1>

  <div class="space-y-2">
    <input
      class="w-full border p-2 rounded text-black text-center"
      placeholder="Your name"
      bind:value={name}
    />
    <textarea
      class="w-full border p-2 rounded text-black text-center"
      placeholder="Your message and avatar url (if none is provided i will use a default one)"
      rows="3"
      bind:value={message}></textarea>
    <button
      class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 disabled:opacity-50"
      on:click={submitMessage}
      disabled={sending || rateLimitRemaining > 0}
    >
      {sending ? 'Sending...' : 'Sign Guestbook'}
    </button>

    {#if error}
      <p class="text-red-600 mt-2">{error}</p>
    {/if}

    {#if rateLimitError}
      <p class="text-red-600 mt-2">{rateLimitError}</p>
    {/if}
  </div>

  <hr />

  <div class="space-y-4">
    {#each entries as entry}
      <div class="flex items-center gap-4 p-4 border rounded shadow">
        <img src={entry.avatar} alt="Avatar" class="w-12 h-12 rounded-full" />
        <div>
          <p class="flex items-center gap-2">
            <span>{entry.name}</span>
            <span class="text-sm text-gray-500">{formatTimestamp(entry.timestamp)}</span>
          </p>
          <p>{entry.message}</p>
        </div>
      </div>
    {/each}
  </div>
</main>
