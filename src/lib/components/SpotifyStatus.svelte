<script>
    import { onMount, onDestroy } from 'svelte';
    import axios from 'axios';
  
    let currentTrack = null;
    let isListening = false;
    let artist = '';
    let track = '';
    let album = '';
    let albumArtUrl = '';
    let progressMs = null; 
    let durationMs = 0;
    let startTime = 0;
    let endTime = 0;
    let interval = null;
  
    const lanyardApiUrl = 'https://api.lanyard.rest/v1/users/442142462857707520';
  
    const fetchSpotifyData = async () => {
      try {
        const response = await axios.get(lanyardApiUrl);
        const data = response.data;
  
        if (data.data && data.data.listening_to_spotify) {
          const timestamp = data.data.spotify.timestamps;
          const newTrack = data.data.spotify;
  
          if (!currentTrack || newTrack.song !== currentTrack.song) {
            if (interval) clearInterval(interval); 
            currentTrack = newTrack;
            artist = currentTrack?.artist || 'Unknown Artist';
            track = currentTrack?.song || 'No Track';
            album = currentTrack?.album || 'Unknown Album';
            albumArtUrl = currentTrack?.album_art_url || '';
            
            startTime = timestamp?.start || 0;  
            endTime = timestamp?.end || 0;
            
            progressMs = 0;
            durationMs = endTime - startTime;
            startProgressInterval();
            isListening = true;
          }
        } else {
          if (interval) clearInterval(interval);
          isListening = false;
          progressMs = null; 
        }
      } catch (error) {
        console.error('Error fetching Spotify data:', error);
        if (interval) clearInterval(interval); 
        isListening = false;
        progressMs = null; 
      }
    };
  
    const formatTime = (timeInMs) => {
      const minutes = Math.floor(timeInMs / 60000);
      const seconds = Math.floor((timeInMs % 60000) / 1000);
      return `${minutes}:${seconds < 10 ? '0' + seconds : seconds}`;
    };
  
    const startProgressInterval = () => {
      interval = setInterval(() => {
        const currentTime = Date.now();
        const elapsed = currentTime - startTime;
        if (elapsed < durationMs) {
          progressMs = elapsed; 
        } else {
          progressMs = durationMs; 
          clearInterval(interval); 
        }
      }, 1000); 
    };
  
    onMount(() => {
      fetchSpotifyData(); 
      const fetchInterval = setInterval(fetchSpotifyData, 5000); 
  
      onDestroy(() => {
        if (interval) clearInterval(interval); 
        clearInterval(fetchInterval); 
      });
    });
  </script>
  
  <div class="max-w-lg mx-auto rounded-lg shadow-lg p-5">
    {#if isListening}
      <div class="flex items-center space-x-4">
        <img src={albumArtUrl} alt="Album Art" class="w-20 h-20 rounded-lg object-cover" />
        <div class="flex flex-col text-white overflow-hidden w-[1000px]">
          <div class="text-xl font-semibold">
            <div class="animate-marquee">
              {track} - {artist}
            </div>
          </div>
          <div class="text-lg text-gray-400 mt-2">
            <div class="animate-marquee">
              {album}
            </div>
          </div>
        </div>
      </div>
  
  
      {#if progressMs !== null} 
        <div class="mt-4 w-full bg-gray-600 rounded-full h-2">
          <div
            class="progress-bar bg-white h-2 rounded-full"
            style="width: {((progressMs / durationMs) * 100).toFixed(2)}%"
          ></div>
        </div>
  
        <div class="flex justify-between text-sm text-gray-300 mt-2">
          <span>{formatTime(progressMs)}</span>
          <span>{formatTime(durationMs)}</span>
        </div>
      {/if}
    {:else}
      <div class="text-gray-400">Not listening to Spotify</div>
    {/if}
  </div>
  
  <style>
    @keyframes marquee {
      0% {
        transform: translateX(100%);
      }
      100% {
        transform: translateX(-100%);
      }
    }
  
    .animate-marquee {
      display: inline-block;
      animation: marquee 12s linear infinite; 
      white-space: nowrap; 
      padding-right: 100%; 
      width: 100%; 
    }
  
    .progress-bar {
      transition: width 0.5s ease; 
    }
  </style>
