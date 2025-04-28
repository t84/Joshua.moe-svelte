<!-- src/lib/components/BDay.svelte -->
<script>
    import { onMount, onDestroy } from 'svelte';
  
    let age = 0;
  
    const birthday = new Date('2002-07-22T00:00:00');
  
    let interval;
  
    function updateAge() {
      const now = new Date();
      const millisecondsInYear = 1000 * 60 * 60 * 24 * 365.2425;
      age = (now - birthday) / millisecondsInYear;
    }
  
    onMount(() => {
      updateAge();
      interval = setInterval(() => {
        updateAge();
      }, 16);
    });
  
    onDestroy(() => {
      clearInterval(interval);
    });
  </script>
  
  <span>{age.toFixed(9)}</span>
  