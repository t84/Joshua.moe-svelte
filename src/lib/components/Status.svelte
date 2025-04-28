<script>
    import { onMount } from 'svelte';
    import axios from 'axios';
    
    let status = 'offline';
    
    const fetchStatus = async () => {
      try {
        const { data } = await axios.get('https://api.lanyard.rest/v1/users/442142462857707520');
        const discordStatus = data.data?.discord_status;
  
        if (discordStatus === 'online' || discordStatus === 'dnd' || discordStatus === 'idle') {
          return 'online'; 
        } else {
          return 'offline'; 
        }
  
      } catch (error) {
        console.error('Error fetching data:', error);
        return 'offline';
      }
    };
    
    onMount(async () => {
      status = await fetchStatus();
    });
  </script>
  
  {#if status === 'online'}
    <p class="text-green-400">I am currently {status}.</p>
  {:else if status === 'offline'}
    <p class="text-red-400">I am currently {status}.</p>
  {/if}
  