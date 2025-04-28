<script>
  import { onMount, onDestroy } from 'svelte';
  import axios from 'axios';

  let currentTrack = null;
  let isListening = false;
  let artist = '';
  let track = '';
  let album = '';
  let albumArtUrl = '';
  let startTime = 0;
  let endTime = 0;
  let durationMs = 0;
  let progressMs = null;
  let interval = null;
  let fetchInterval = null;

  const fetchSpotifyData = async () => {
  try {
    const { data } = await axios.get('https://api.lanyard.rest/v1/users/442142462857707520');
    const spotify = data.data?.spotify;

    if (spotify) {
      if (!currentTrack || spotify.song !== currentTrack.song) {
        // New song
        if (interval) clearInterval(interval);
        currentTrack = spotify;
        if (typeof localStorage !== 'undefined') {
          localStorage.setItem('currentTrack', JSON.stringify({
            ...spotify,
            timestamps: spotify.timestamps
          }));
        }
        artist = spotify.artist;
        track = spotify.song;
        album = spotify.album;
        albumArtUrl = spotify.album_art_url;
        startTime = spotify.timestamps.start;
        endTime = spotify.timestamps.end;
        durationMs = endTime - startTime;
        progressMs = Date.now() - startTime;
        isListening = true;
        startProgressInterval();
      } else {
        startTime = spotify.timestamps.start;
        endTime = spotify.timestamps.end;
        durationMs = endTime - startTime;
        progressMs = Date.now() - startTime;
      }
    } else {
      resetState();
    }
  } catch {
    resetState();
  }
};

  const startProgressInterval = () => {
    interval = setInterval(() => {
      const now = Date.now();
      const elapsed = now - startTime;
      progressMs = Math.min(elapsed, durationMs);
      if (progressMs >= durationMs) clearInterval(interval);
    }, 1000);
  };

  const resetState = () => {
    clearInterval(interval);
    if (typeof localStorage !== 'undefined') {
      localStorage.removeItem('currentTrack');
    }
    currentTrack = null;
    artist = '';
    track = '';
    album = '';
    albumArtUrl = '';
    progressMs = null;
    durationMs = 0;
    isListening = false;
  };

  const formatTime = (ms) => {
    const m = Math.floor(ms / 60000);
    const s = Math.floor((ms % 60000) / 1000);
    return `${m}:${s < 10 ? '0' : ''}${s}`;
  };

  onMount(() => {
    if (typeof localStorage !== 'undefined') {
      const stored = localStorage.getItem('currentTrack');
      if (stored) {
        const parsed = JSON.parse(stored);
        currentTrack = parsed;
        artist = parsed.artist;
        track = parsed.song;
        album = parsed.album;
        albumArtUrl = parsed.album_art_url;
        startTime = parsed.timestamps.start;
        endTime = parsed.timestamps.end;
        durationMs = endTime - startTime;
        progressMs = Date.now() - startTime;
        isListening = true;
        startProgressInterval();
      }
    }
    fetchSpotifyData();
    fetchInterval = setInterval(fetchSpotifyData, 2000);
  });

  onDestroy(() => {
    clearInterval(interval);
    clearInterval(fetchInterval);
  });
</script>

<div class="w-full rounded-lg p-6">
  {#if isListening}
    <div class="flex flex-col text-left space-y-4">
      <div class="flex items-start space-x-4">
        <img src={albumArtUrl} alt="Album Art" class="w-20 h-20 rounded-lg object-cover flex-shrink-0" />
        <div class="flex flex-col justify-center text-white overflow-hidden w-full text-left">
          <div class="text-xl font-semibold overflow-hidden text-ellipsis whitespace-nowrap">
            {track} - {artist}
          </div>
          <div class="text-lg text-gray-400 mt-2 overflow-hidden text-ellipsis whitespace-nowrap">
            {album}
          </div>
        </div>
      </div>

      {#if progressMs !== null}
        <div class="w-full bg-gray-600 rounded-full h-2">
          <div class="progress-bar bg-white h-2 rounded-full" style="width: {((progressMs / durationMs) * 100).toFixed(2)}%"></div>
        </div>
        <div class="flex justify-between text-sm text-gray-300">
          <span>{formatTime(progressMs)}</span>
          <span>{formatTime(durationMs)}</span>
        </div>
      {/if}
    </div>
  {:else}
    <div class="text-gray-400 text-center">Not listening to any music.</div>
  {/if}
</div>

<style>
  .progress-bar {
    transition: width 0.5s ease;
  }
  .overflow-hidden {
    overflow: hidden;
  }
  .text-ellipsis {
    text-overflow: ellipsis;
  }
  .whitespace-nowrap {
    white-space: nowrap;
  }
</style>



