# nonhumanworks

## Generated Artworks

Read more about the tech here: https://towardsdatascience.com/generating-modern-arts-using-generative-adversarial-network-gan-on-spell-39f67f83c7b4

### What

You can access and send prompts via the api and get an image back within about 5 minutes.

### Tech

Queue: Redis

API: Python-Flask

Web: basic html & php for the gallery display

### Images

The images are 256x256px due to the constraints on only having 12GB gpu available. If we had 16GB we would be able to do 512x512.

### Examples

Prompt "time reversal"

![time-reversal](https://user-images.githubusercontent.com/616585/154299789-4951b9fb-5a7c-43b4-9f42-8fff364ee951.png)

Prompt "watercolor drones in the sky"

![watercolor-drones](https://user-images.githubusercontent.com/616585/154299595-b197ae43-493a-4a09-9a03-f72f71274e3c.png)

### Workflow

1. Prompt is added via api
2. Redis queue set populated
3. Every minute cron checks for items in queue and then processes one by on in queue
4. current key set to current working
5. busy key set
6. image created
7. cron checking for images every minute to sshuttle to static image server
8. busy key unset
9. current key set to "taking a break"

### Workflow diagram

![nonhumanworks-architecture-diagram](https://user-images.githubusercontent.com/616585/165548891-45859778-eaeb-43ac-87ea-559e6c1b2ada.png)


