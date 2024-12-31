from pydub import AudioSegment
import time

# AudioSegment.converter = "/usr/local/bin/ffmpeg"

inbound = AudioSegment.from_wav("./data/inbound/example.wav")

timeline = [
    {
      "message": 'ブーブー',
      "started_sec": 0,
      "ended_sec": 1.10376,
      "speaker_type": 'INBOUND',
      "status": 'DONE',
      "created_at": '2024-12-23T16:13:11.240Z',
    },
    {
      "message": 'ん',
      "started_sec": 1.10376,
      "ended_sec": 1.79928,
      "speaker_type": 'INBOUND',
      "status": 'DONE',
      "created_at": '2024-12-23T16:13:11.247Z',
    },
    {
      "message": 'ん',
      "started_sec": 1.79928,
      "ended_sec": 2.88792,
      "speaker_type": 'INBOUND',
      "status": 'DONE',
      "created_at": '2024-12-23T16:13:11.253Z',
    },
    {
      "message": 'ん',
      "started_sec": 2.88792,
      "ended_sec": 4.339440000000001,
      "speaker_type": 'INBOUND',
      "status": 'DONE',
      "created_at": '2024-12-23T16:13:11.260Z',
    },
    {
      "message": 'ん',
      "started_sec": 4.339440000000001,
      "ended_sec": 6.0933600000000006,
      "speaker_type": 'INBOUND',
      "status": 'DONE',
      "created_at": '2024-12-23T16:13:11.273Z',
    },
    {
      "message": 'ん',
      "started_sec": 6.0933600000000006,
      "ended_sec": 6.38064,
      "speaker_type": 'INBOUND',
      "status": 'DONE',
      "created_at": '2024-12-23T16:13:11.279Z',
    },
    {
      "message": 'ん',
      "started_sec": 6.38064,
      "ended_sec": 6.728400000000001,
      "speaker_type": 'INBOUND',
      "status": 'DONE',
      "created_at": '2024-12-23T16:13:11.284Z',
    },
    {
      "message": 'ん',
      "started_sec": 6.728400000000001,
      "ended_sec": 6.788880000000001,
      "speaker_type": 'INBOUND',
      "status": 'DONE',
      "created_at": '2024-12-23T16:13:11.290Z',
    },
    {
      "message": 'ん',
      "started_sec": 6.788880000000001,
      "ended_sec": 7.182,
      "speaker_type": 'INBOUND',
      "status": 'DONE',
      "created_at": '2024-12-23T16:13:11.297Z',
    },
    {
      "message": 'ん',
      "started_sec": 7.182,
      "ended_sec": 7.72632,
      "speaker_type": 'INBOUND',
      "status": 'DONE',
      "created_at": '2024-12-23T16:13:11.305Z',
    },
    {
      "message": 'ん',
      "started_sec": 11.975039999999998,
      "ended_sec": 13.033439999999999,
      "speaker_type": 'INBOUND',
      "status": 'DONE',
      "created_at": '2024-12-23T16:13:11.311Z',
    },
    {
      "message": 'ん',
      "started_sec": 13.033439999999999,
      "ended_sec": 13.320720000000001,
      "speaker_type": 'INBOUND',
      "status": 'DONE',
      "created_at": '2024-12-23T16:13:11.316Z',
    },
    {
      "message": 'ん',
      "started_sec": 13.320720000000001,
      "ended_sec": 13.39632,
      "speaker_type": 'INBOUND',
      "status": 'DONE',
      "created_at": '2024-12-23T16:13:11.322Z',
    },
    {
      "message": 'ん',
      "started_sec": 13.39632,
      "ended_sec": 14.227920000000001,
      "speaker_type": 'INBOUND',
      "status": 'DONE',
      "created_at": '2024-12-23T16:13:11.329Z',
    },
    {
      "message": '社長はいらっしゃいますか？',
      "speaker_type": 'OUTBOUND',
      "file": './data/outbound/社長はいらっしゃいますか？.wav',
      "status": 'DONE',
      "created_at": '2024-12-23T16:13:11.352Z',
    },
    {
      "message": 'おー、ミックスがないね',
      "started_sec": 14.227920000000001,
      "ended_sec": 17.372880000000002,
      "speaker_type": 'INBOUND',
      "status": 'DONE',
      "created_at": '2024-12-23T16:13:24.534Z',
    },
    {
      "message": 'あ、ある',
      "started_sec": 20.21544,
      "ended_sec": 20.95632,
      "speaker_type": 'INBOUND',
      "status": 'DONE',
      "created_at": '2024-12-23T16:13:24.541Z',
    },
    {
      "message": 'ありがとうございます、よろしくお願いします',
      "speaker_type": 'OUTBOUND',
      "file": './data/outbound/ありがとうございます。よろしくお願いいたします。.wav',
      "status": 'DONE',
      "created_at": '2024-12-23T16:13:24.686Z',
    },
    {
      "message": '今、聞こえますか?',
      "started_sec": 23.874480000000002,
      "ended_sec": 24.751440000000002,
      "speaker_type": 'INBOUND',
      "status": 'DONE',
      "created_at": '2024-12-23T16:13:37.955Z',
    },
    {
      "message": '1、2、3',
      "started_sec": 26.611200000000004,
      "ended_sec": 27.76032,
      "speaker_type": 'INBOUND',
      "status": 'DONE',
      "created_at": '2024-12-23T16:13:37.968Z',
    },
    {
      "message": 'アロー、アロー',
      "started_sec": 30.935520000000004,
      "ended_sec": 33.52104,
      "speaker_type": 'INBOUND',
      "status": 'DONE',
      "created_at": '2024-12-23T16:13:37.974Z',
    },
    {
      "message": '聞こえますか?',
      "started_sec": 33.52104,
      "ended_sec": 36.95328,
      "speaker_type": 'INBOUND',
      "status": 'DONE',
      "created_at": '2024-12-23T16:13:37.980Z',
    },
    {
      "message": 'ありがとうございます、よろしくお願いします',
      "speaker_type": 'OUTBOUND',
      "file": './data/outbound/ありがとうございます。よろしくお願いいたします。.wav',
      "status": 'TODO',
      "created_at": '2024-12-23T16:13:38.761Z',
    },
    {
      "message": '4,5,6',
      "started_sec": 36.95328,
      "ended_sec": 38.4048,
      "speaker_type": 'INBOUND',
      "status": 'DONE',
      "created_at": '2024-12-23T16:13:38.950Z',
    },
    {
      "message": 'アロー',
      "started_sec": 39.70512,
      "ended_sec": 40.46112,
      "speaker_type": 'INBOUND',
      "status": 'DONE',
      "created_at": '2024-12-23T16:13:39.446Z',
    },
    {
      "message": 'アロー',
      "started_sec": 40.46112,
      "ended_sec": 41.17176,
      "speaker_type": 'INBOUND',
      "status": 'DONE',
      "created_at": '2024-12-23T16:13:39.897Z',
    },
  ]

# Khởi tạo comined sound
combined_sound = AudioSegment.silent(duration=0)

for index, entry in enumerate(timeline):
  # Trường hợp là INBOUND
  if(entry["speaker_type"] == 'INBOUND'):
    start_ms = float(entry["started_sec"] * 1000)
    end_ms = float(entry["ended_sec"] * 1000)
    entry["audio"] = inbound[start_ms:end_ms]

  # Trường hợp là OUTBOUND
  else:
    audio = AudioSegment.from_file(entry["file"]) 
    entry["audio"] = audio

  # Check item audio trong entry
  if "audio" in entry:
    combined_sound += entry["audio"]

# Xuất file âm thanh sau khi combine  
timestamp = int(time.time()) 
combined_sound.export(f"./output-not-has-silent-{timestamp}.wav", format="wav")

