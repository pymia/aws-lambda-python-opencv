import cv2
import json

def lambda_handler(event, context):
	img = cv.imread(cv.samples.findFile("test.jpeg"))
	if img is None:
		print("Could not read the image.")
	return {
		'statusCode': 200,
		'body': json.dumps('Hello from Lambda!')
	}

if __name__ == "__main__":
	lambda_handler(42, 42)