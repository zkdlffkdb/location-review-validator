import styles from "./SampleCards.module.css";
import { React, useState } from "react";

function SampleCards() {
  return (
    <div className={styles.cardsContainer}>
      <div className={styles.reviewCard}>
        <h2 className={styles.title}>Legitimate review</h2>
        <div className={styles.metadata}>
          <span className={`${styles.badge} ${styles.legitimate}`}>
            Legitimate
          </span>
          <span>@ Yakiniku Like, Paya Lebar Quarter</span>
        </div>
        <p className={styles.rating}>Rating: 5/5</p>
        <p className={styles.reviewText}>
          "Had an amazing dinner at this restaurant last night! The food was
          great and the service was excellent. The atmosphere was cozy and
          romantic, perfect for our anniversary. The staff was attentive without
          being intrusive. Will definitely be coming back soon. Highly
          recommended!"
        </p>
        <p className={styles.reviewText}>
          <b>save the JSON file below to test our review analyser:</b>
        </p>
        <a className={styles.reviewText} href="/yakinikuLike.json" download>
          download JSON file
        </a>
      </div>
      <div className={styles.reviewCard}>
        <h2 className={styles.title}>Irrelevant review</h2>
        <div className={styles.metadata}>
          <span className={`${styles.badge} ${styles.irrelevant}`}>
            Irrelevant
          </span>
          <span>@ Mixue, Yew Tee Point</span>
        </div>
        <p className={styles.rating}>Rating: 5/5</p>
        <p className={styles.reviewText}>
          "I love my new iPhone 15! The camera quality is amazing and the
          battery life is so much better than my old phone. Unfortunately, I ate
          my ice cream too quickly and could not test all the camera features of
          my phone. Overall happy with my purchase."
        </p>
        <p className={styles.reviewText}>
          <b>save the JSON file below to test our review analyser:</b>
        </p>
        <a className={styles.reviewText} href="/mixue.json" download>
          download JSON file
        </a>
      </div>
    </div>
  );
}

export default SampleCards;