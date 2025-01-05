VOCAL PAGES

# Introduction:

**Vocal Pages** is an innovative device designed to make books and
novels accessible to visually impaired individuals. Equipped with
built-in Wi-Fi, voice input, and text-to-speech capabilities, it allows
users to search for and **listen to books** stored on an online library.
The device fetches content directly from a server in text or audiobook
format and reads it aloud with **high-quality audio**.

# Hardware Requirements:

1\. Rasberry pi (4) or above

2\. SD-card (for pi os)

3\. Mic

5\. Headphones/Speaker

# Server HLD

We can build an API which will allow clients to retrive audio book of
requested book name given they are available in our database. FASTAPI
for building Api with Relational Database

### 1.2 DATABASE HLD {#database-hld}

We will use file system (AWS S3 buckets) since audio files are storage
intensive. The Database will only store the file-path of audio book and
other necessary details

### 1.2 Why are we saving audio files over TTS on client side? {#why-are-we-saving-audio-files-over-tts-on-client-side}

Text to speech model is good option too but it will be more resource
extensive on client side hence making the user experience worse and
hardware dependent.

Storing audio files on a server will allow us to scale more efficiently
and this will ensure the quailty of each audio book for multiple clients

### 1.3 Server Hosting {#server-hosting}

AWS EC2 will be used to host the FASTApi and Aamazon RDBMS for hosting
database while S3 buckets for storing large audio books (we can compress
them while storing and decompress on client side for better performance)

# Client HLD

As of now I m planning on writting client side software using python and
using its rich library ecosystem for speech recognization and calling
the server api

we can download an audio player to read the book which will use speaker
as its output device

