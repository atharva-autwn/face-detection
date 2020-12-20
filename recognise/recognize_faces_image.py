import face_recognition
import argparse
import pickle
import cv2


def recognize(testimg):
	with open(r'recognise\encodings.pickle','rb') as input:
		data = pickle.load(input)

	image = testimg
	rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

	boxes = face_recognition.face_locations(rgb,
		model="cnn" )
	encodings = face_recognition.face_encodings(rgb, boxes)

	names = []

	for encoding in encodings:
		matches = face_recognition.compare_faces(data["encodings"],
			encoding)
		name = "Unknown"

		if True in matches:
			matchedIdxs = [i for (i, b) in enumerate(matches) if b]
			counts = {}

			for i in matchedIdxs:
				name = data["names"][i]
				counts[name] = counts.get(name, 0) + 1
			name = max(counts, key=counts.get)

		names.append(name)
	return names

#print(recognize())