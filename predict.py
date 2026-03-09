#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: okokprojects
"""

import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import json


class resultclassification:
    def __init__(self, filename):
        self.filename = filename
        self.model = load_model('model_food.h5')

    def prediction(self):
        try:
            test_image = image.load_img(self.filename, target_size=(300, 300))
            test_image = image.img_to_array(test_image)
            test_image = test_image / 255
            test_image = np.expand_dims(test_image, axis=0)

            result = self.model.predict(test_image)
            class_index = np.argmax(result)

            # ---------- FIXED NUTRITION: ONLY NUMBERS ----------
            predictions = {
                0: {
                    "food": "Biriyani",
                    "classification": "Food",
                    "calories": 420,
                    "carbs": 55,
                    "protein": 14,
                    "fat": 12,
                    "details": "Calories vary based on ingredients like chicken, egg or veg.",
                    "consume": "Suitable for most people.",
                    "not_consume": "Avoid if gluten intolerant or on low-carb diet.",
                    "fat_consumption": "Moderate to high fat.",
                    "diabetes": "High carbs — not ideal for diabetics.",
                    "cholesterol": "Can increase cholesterol due to oils."
                },

                1: {
                    "food": "Chappathi",
                    "classification": "Food",
                    "calories": 104,
                    "carbs": 63,
                    "protein": 3,
                    "fat": 3,
                    "details": "Whole wheat chapathi, healthy fiber-rich food.",
                    "consume": "Good for weight loss & diabetics in moderation.",
                    "not_consume": "Avoid if gluten sensitive.",
                    "fat_consumption": "Low fat.",
                    "diabetes": "Better than rice but still moderate carbs.",
                    "cholesterol": "Safe & low cholesterol."
                },

                2: {
                    "food": "Dosa",
                    "classification": "Food",
                    "calories": 133,
                    "carbs": 75,
                    "protein": 11,
                    "fat": 47,
                    "details": "South Indian fermented food, gives good energy.",
                    "consume": "Suitable for most people.",
                    "not_consume": "Avoid if gluten intolerant depending on preparation.",
                    "fat_consumption": "Can be high depending on oil used.",
                    "diabetes": "High carbs — limit intake.",
                    "cholesterol": "High fat may raise levels."
                },

                3: {
                    "food": "Idly",
                    "classification": "Food",
                    "calories": 58,
                    "carbs": 12,
                    "protein": 2,
                    "fat": 1,
                    "details": "Very healthy steamed food, light for digestion.",
                    "consume": "Good for all age groups.",
                    "not_consume": "None specific.",
                    "fat_consumption": "Very low fat.",
                    "diabetes": "Good choice for diabetics.",
                    "cholesterol": "Very low."
                },

                4: {
                    "food": "Foxtail Millet Pongal",
                    "classification": "Food",
                    "calories": 150,
                    "carbs": 28,
                    "protein": 5,
                    "fat": 4,
                    "details": "Millet-based, rich in fiber, diabetic-friendly.",
                    "consume": "Recommended for diabetics & weight loss.",
                    "not_consume": "None.",
                    "fat_consumption": "Low fat.",
                    "diabetes": "Very suitable.",
                    "cholesterol": "Low."
                },

                5: {
                    "food": "Pongal",
                    "classification": "Food",
                    "calories": 200,
                    "carbs": 35,
                    "protein": 6,
                    "fat": 5,
                    "details": "Traditional South Indian breakfast.",
                    "consume": "Healthy when eaten with less ghee.",
                    "not_consume": "Avoid if allergic to lentils.",
                    "fat_consumption": "Moderate depending on ghee.",
                    "diabetes": "Consume in moderation.",
                    "cholesterol": "Low unless extra ghee is added."
                },

                6: {
                    "food": "Ragi Dosa",
                    "classification": "Food",
                    "calories": 120,
                    "carbs": 20,
                    "protein": 4,
                    "fat": 3,
                    "details": "Rich in calcium and fiber.",
                    "consume": "Good for diabetics.",
                    "not_consume": "Avoid if gluten sensitive depending on ingredients.",
                    "fat_consumption": "Low.",
                    "diabetes": "Recommended.",
                    "cholesterol": "Low cholesterol."
                },

                7: {
                    "food": "Ragi Idly",
                    "classification": "Food",
                    "calories": 70,
                    "carbs": 14,
                    "protein": 3,
                    "fat": 1,
                    "details": "Healthy steamed ragi breakfast.",
                    "consume": "Excellent for diabetics.",
                    "not_consume": "None.",
                    "fat_consumption": "Low.",
                    "diabetes": "Very diabetic-friendly.",
                    "cholesterol": "Very low."
                },

                8: {
                    "food": "Rice",
                    "classification": "Food",
                    "calories": 130,
                    "carbs": 28,
                    "protein": 2.5,
                    "fat": 0.3,
                    "details": "Common staple food; high in carbs.",
                    "consume": "Suitable for most people.",
                    "not_consume": "Avoid excess if diabetic.",
                    "fat_consumption": "Very low fat.",
                    "diabetes": "High GI — consume carefully.",
                    "cholesterol": "Negligible."
                }
            }

            prediction = predictions.get(class_index, {
                "classification": "Unknown",
                "food": "Unknown",
                "calories": 0,
                "carbs": 0,
                "protein": 0,
                "fat": 0,
                "details": "Could not recognize the food."
            })

            return json.dumps(prediction)

        except Exception as e:
            print("Error during prediction:", e)
            return json.dumps({
                "classification": "Error",
                "food": "Error",
                "calories": 0,
                "carbs": 0,
                "protein": 0,
                "fat": 0,
                "details": "An error occurred."
            })
